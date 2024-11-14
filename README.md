# Code Combiner Tool

This tool recursively scans a directory and its subdirectories, combining all readable code files into a single output file. It is particularly useful for developers who need to consolidate code snippets from multiple files.

## Features
- **Recursive Scanning**: Combines files from the main directory and all subdirectories.
- **Customizable Extensions**: Supports commonly used extensions and allows custom input.
- **Encoding Handling**: Handles UTF-8 and ISO-8859-1 encodings for broad compatibility.

## Installation

Clone this repository and ensure you have Python 3 installed.

## Usage
### Run the script with customizable options for input directory, output file, and file extensions.
```bash
python3 combine.py -i <input_directory> -o <output_file> -e <extensions>
```
### Examples
Combine all readable files in the current directory:
```bash
python3 combine.py
```
### Specify a custom input directory and output file:
```bash
python3 combine.py -i ./src -o {file_name}
```
### Include only specific file types:
```bash
python3 combine.py -e .json .ts .html
```
