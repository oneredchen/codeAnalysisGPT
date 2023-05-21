# Code Analysis Tool

This is a tool for analyzing code files and generating a README.md file based on the code analysis. The tool uses OpenAI's language model and a PromptTemplate to analyze and explain code snippets.

## Setup

1. Clone this repository:

   ```
   git clone https://github.com/username/repo.git
   cd repo/
   ```

2. Install the required Python packages:

   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file and add your OpenAI API key:

   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

1. Place the code file to analyze in the `code_for_analysis` folder.

2. Run the tool:

   ```
   python main.py
   ```

3. The tool will prompt for the filename to analyze (`eg. test.py`). Enter the filename and press Enter to proceed.

4. The tool will generate two output files:

   - `code_analysis_output/analyzed_code.[file_extension]`: Contains the deobfuscated code.
   - `code_analysis_output/README.md`: Contains the explanation of the analyzed code.

## How it works

The tool reads the code file and extracts the code snippet to analyze. The code is then fed into OpenAI's language model to deobfuscate it using a PromptTemplate. The deobfuscated code is passed into another PromptTemplate to generate a README.md file that explains how the code works.

## License

This tool is licensed under the [MIT License](LICENSE).