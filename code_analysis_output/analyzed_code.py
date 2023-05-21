import os
import openai
from dotenv import load_dotenv

# Constants
INPUT_PATH = os.path.join(os.getcwd(), "code_for_analysis")
OUTPUT_PATH = os.path.join(os.getcwd(), "code_analysis_output")

# Load environment variables
load_dotenv()

# Retrieve the OpenAI API key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")


def analyze_code(code, file_extension):
    prompt = f"The following code is extracted from a {file_extension} file. Please help me deobfuscate and improve the following code snippet:\n{code}\n"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
    )
    analyzed_code = response.choices[0].text.strip()

    return analyzed_code


def explain_code(code, file_extension):
    prompt = f"Please generate a README.md file based on the {file_extension} code:\n{code}\n Your answer should be properly structured."
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
    )
    explanation = response.choices[0].text.strip()

    return explanation


def main():
    # Retrieve the file path
    filename = input("Please provide the filename for analysis: ")
    filepath = os.path.join(INPUT_PATH, filename)

    # Get the file extension
    file_extension = os.path.splitext(filename)[1]
    print(f"File Extension: {file_extension}")

    try:
        with open(filepath, "r") as file:
            code = file.read()

        analyzed_code = analyze_code(code, file_extension)
        explanation = explain_code(analyzed_code, file_extension)

        # Write the analyzed code to a file with the same extension as the input file
        analyzed_code_filepath = os.path.join(
            OUTPUT_PATH, f"analyzed_code{file_extension}"
        )
        with open(analyzed_code_filepath, "w") as output_file:
            output_file.write(analyzed_code)

        # Write the explanation to a README.md file
        explanation_filepath = os.path.join(OUTPUT_PATH, "README.md")
        with open(explanation_filepath, "w") as output_file:
            output_file.write(explanation)

        print("Script End")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
