#!/usr/bin/env python3

import time
import json
from base64 import b64encode
from os.path import join
import csv
import os

import requests  # To install requests, use: pip install requests
import urllib3

# Configuration
protocol = "https"
host = "[INSERT HOSTNAME]"
port = "[INSERT PORT]"
user = "[INSERT USERNAME]"
password = "[INSERT PASSWORD]"

# output_path = '/home/gen/sca'
# output_filename = 'sca_list.csv'
output_path = os.getcwd()
output_filename = os.path.join(output_path, "sca_list_session.csv")

# Variables
base_url = f"{protocol}://{host}:{port}"
login_url = f"{base_url}/security/user/authenticate"
basic_auth = f"{user}:{password}".encode()
login_headers = {"Authorization": f"Basic {b64encode(basic_auth).decode()}"}

# Disable insecure https warnings (for self-signed SSL certificates)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# Functions
def authenticate(session):
    resp = session.get(login_url, headers=login_headers, verify=False)
    if resp.status_code == 200:
        token = resp.json()["data"]["token"]
        return {"Authorization": f"Bearer {token}"}
    else:
        raise Exception(f"Error obtaining authentication token: {resp.json()}")


def get_response(url, session, verify=False):
    """Get API result"""
    request_result = session.get(url, verify=verify)
    if request_result.status_code == 200:
        return json.loads(request_result.content.decode())
    elif request_result.status_code == 401:
        print("Re-acquiring JWT....")
        session.headers.update(authenticate(session))
        return get_response(url, session=session)
    else:
        raise Exception(f"Error obtaining response: {request_result.json()}")


def write_csv(data):
    try:
        with open(
            join(output_path, output_filename), "w", encoding="utf-8", newline=""
        ) as outfile:
            writer = csv.DictWriter(
                outfile,
                fieldnames=[
                    "agent_name",
                    "reason",
                    "remediation",
                    "description",
                    "result",
                    "title",
                    "condition",
                    "references",
                    "rationale",
                    "registry",
                    "status",
                    "agent_group",
                ],
            )
            writer.writeheader()
            for row in data:
                writer.writerow(row)
        print(f'\nReport created at "{join(output_path, output_filename)}".')
    except Exception as e:
        print(
            f"Following error was found while writing report at {join(output_path, output_filename)}: {e}. "
        )
        response = input("Do you want the report to be displayed here? [y/n]: ")
        if response == "y":
            print(data)
        else:
            print("Exiting...")


def main():
    with requests.Session() as session:
        result = []
        session.headers.update(authenticate(session))
        # Request
        agents = get_response(
            base_url
            + "/agents?wait_for_complete=true&select=name&select=status&select=group&limit=100000",
            session=session,
        )
        if agents["data"]["total_affected_items"] == 0:
            print(f"No agents were found: \n{agents}")
            exit(0)

        for agent_data in agents["data"]["affected_items"]:
            if agent_data["status"] == "never_connected":
                print(
                    f'Status of "{agent_data["name"]}" agent is "never_connected" so their SCA state is unknown. '
                    f"Skipping..."
                )
                continue

            print(
                f'Getting SCA information for agent {agent_data["id"]}: {agent_data["name"]}'
            )

            try:
                policies = get_response(
                    base_url
                    + f'/sca/{agent_data["id"]}?wait_for_complete=true&limit=100000',
                    session=session,
                )
            except Exception as wazuh_error:
                print(
                    f'Could not get sca policy information from Agent {agent_data["name"]} ({agent_data["id"]}). '
                    f"Wazuh error = {wazuh_error}"
                )
                continue

            for policy in policies["data"]["affected_items"]:
                try:
                    scas = get_response(
                        base_url
                        + f'/sca/{agent_data["id"]}/checks/{policy["policy_id"]}?wait_for_complete=true&select=result,title,status,compliance&limit=100000',
                        session=session,
                    )
                except Exception as wazuh_error:
                    print(
                        f'Could not get package information from Agent {agent_data["name"]} ({agent_data["id"]}). '
                        f"Wazuh error = {wazuh_error}"
                    )
                    continue

                try:
                    result.extend(
                        [
                            {
                                "agent_name": agent_data.get("name", "unknown"),
                                "result": sca.get("result", "unknown"),
                                "title": sca.get("title", "unknown"),
                                "status": sca.get("status", "unknown"),
                                "compliance": sca.get("compliance", "unknown"),
                                "agent_group": agent_data.get("group", "unknown"),
                            }
                            for sca in scas["data"]["affected_items"]
                        ]
                    )
                except Exception as e:
                    print(
                        f'An error was found while parsing "{agent_data["name"]}" agent packages: {e}. Skipping...'
                    )

    write_csv(result)


if __name__ == "__main__":
    startTime = time.time()
    main()
    executionTime = time.time() - startTime
    print("Execution time in seconds: " + str(executionTime))
