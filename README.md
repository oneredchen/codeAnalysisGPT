# Code Analysis and Explanation

This repository contains a Python script that uses the LangChain library to deobfuscate and explain code.

# Overview

The script performs two main operations:

1. `Code Analysis`: It takes a code file as input, deobfuscates it, and writes the analyzed code to an output file.

2. `Code Explanation`: It generates an explanation of the analyzed code and writes it to a README.md file.

The LangChain library's OpenAI model is used to perform both operations. The model's temperature parameter is set to 0.1 to ensure the output is deterministic and reliable.

# Getting Started

## Prerequisites

To run the script, you need the following:

- Python 3.6 or higher.
- OpenAI API key.
- LangChain Python library.
- python-dotenv library.

# Installation

1. Clone the repository:

   ```
   git clone https://github.com/oneredchen/codeAnalysisGPT.git
   ```

2. Navigate to the project directory:

   ```
   cd codeAnalysisGPT
   ```

3. Create a Python virtual environment and activate it:

   ```
   python3 -m venv env
   source env/bin/activate
   ```

4. Install the necessary Python libraries from the `requirements.txt` file:

   ```
   pip install -r requirements.txt
   ```

5. Create a .env file in your project root and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your-api-key-here
   ```

# Usage

1. Place the code file you want to analyze in the code_for_analysis directory.

2. Run the script and provide the filename when prompted:

   ```
   python main.py
   ```

The script will write the analyzed code to a new file in the `code_analysis_output` directory and the explanation to a `README.md` file.

# Output

The script outputs two files:

1. `analyzed_code.<file_extension>`: Contains the deobfuscated code.
2. `README.md`: Contains an explanation of the analyzed code.

# Error Handling

The script handles any exceptions that occur during file handling or code analysis, and outputs an error message if an exception is caught.
