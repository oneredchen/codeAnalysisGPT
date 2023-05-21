import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

# Constants
INPUT_PATH = os.path.join(os.getcwd(),"code_for_analysis")
OUTPUT_PATH = os.path.join(os.getcwd(),"code_analysis_output")

# Load environment variables
load_dotenv()

# Retrieve the OpenAI API key from the environment variable
openai_api_key = os.getenv("OPENAI_API_KEY")

def analyze_code(code, file_extension):
    llm = OpenAI(temperature=0.1)
    prompt = PromptTemplate(input_variables=["file_extension", "code"], template="The following code is extracted from a {file_extension} file. Please help me deobfuscate the following code snippet:\n{code}\n Return only the deobfuscated")
    chain = LLMChain(llm=llm, prompt=prompt)
    analyzed_code = chain.run({"file_extension": file_extension, "code": code})
    return analyzed_code

def explain_code(code, file_extension):
    llm = OpenAI(temperature=0.1)
    prompt = PromptTemplate(input_variables=["file_extension", "code"], template="Please generate a README.md file based on the {file_extension} code:\n{code}\n")
    chain = LLMChain(llm=llm, prompt=prompt)
    explanation = chain.run({"file_extension": file_extension, "code": code})
    return explanation

def main():
    filename = input("Please provide the filename for analysis eg. test.py: ")
    filepath = os.path.join(INPUT_PATH, filename)

    file_extension = os.path.splitext(filename)[1]
    print(f"File Extension: {file_extension}")

    try:
        with open(filepath, 'r') as file:
            code = file.read()

        analyzed_code = analyze_code(code, file_extension)
        explanation = explain_code(analyzed_code, file_extension)

        analyzed_code_filepath = os.path.join(OUTPUT_PATH, f'analyzed_code{file_extension}')
        with open(analyzed_code_filepath, 'w') as output_file:
            output_file.write(analyzed_code)

        explanation_filepath = os.path.join(OUTPUT_PATH, 'README.md')
        with open(explanation_filepath, 'w') as output_file:
            output_file.write(explanation)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()