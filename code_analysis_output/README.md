# Deobfuscated Code Analyzer

This script reads a file, analyzes and deobfuscates its content using OpenAI's GPT-3, generates a README.md file to document the file, and outputs the analyzed code and README.md to the output directory.

## Prerequisites

- Python 3.x
- OpenAI API key (retrieve it from the environment variable `OPENAI_API_KEY`)

## Installation

1. Clone the repository
2. Install the required packages using `pip install -r requirements.txt`
3. Set your `OPENAI_API_KEY` environment variable

## Usage

1. Place the code to be analyzed in the `code_for_analysis` directory
2. Run the script using `python main.py`
3. Provide the filename when prompted (including the file extension)
4. The script will analyze and deobfuscate the code using the `text-davinci-002` model of OpenAI's GPT-3
5. The analyzed code will be output to the `code_analysis_output` directory with the same file extension as the input file
6. The script will generate a README.md file that explains how the original code was transformed and includes the deobfuscated code
7. The README.md file will also be output to the `code_analysis_output` directory

## Output

The `code_analysis_output` directory will contain the following files:

1. `analyzed_code.{file_extension}`: The analyzed and deobfuscated code from the input file
2. `README.md`: A detailed explanation of the analyzed code

## Contributing

Contributions are welcome! Please create a pull request with any suggested changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.