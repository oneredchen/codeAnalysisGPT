    # Make a POST request to the login URL
    response = session.post(login_url, headers=login_headers, verify=False)
   
    # Check if the response is successful
    if response.status_code == 200:
        print("Authentication successful")
    else:
        print("Authentication failed")
        exit()

# README

This project contains a .py code that configures a connection to a hostname, port, username, and password. It also contains functions to authenticate the connection.

## Requirements

- Python 3.x
- urllib3

## Configuration

The following variables must be configured before running the code:

- protocol: The protocol used for the connection (e.g. https)
- host: The hostname of the server
- port: The port of the server
- user: The username used for authentication
- password: The password used for authentication
- output_path: The path to the output file
- output_filename: The name of the output file

## Usage

To use the code, run the following command:

```
python3 <