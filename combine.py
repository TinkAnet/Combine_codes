import os
import argparse

def combine_code_files(input_directory, output_file, extensions):
    files_combined = 0  # Track the number of files processed
    readable_extensions = set(extensions)
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for root, _, files in os.walk(input_directory):
            for filename in files:
                file_path = os.path.join(root, filename)

                # Skip the current script file and non-readable extensions
                if filename == 'combine.py' or not any(filename.endswith(ext) for ext in readable_extensions):
                    continue
                
                # Process readable files
                if os.path.isfile(file_path):
                    try:
                        with open(file_path, 'r', encoding='utf-8') as infile:
                            code = infile.read()
                        print(f"Successfully read {file_path} with UTF-8 encoding")
                    except UnicodeDecodeError:
                        with open(file_path, 'r', encoding='ISO-8859-1') as infile:
                            code = infile.read()
                        print(f"Successfully read {file_path} with ISO-8859-1 encoding")

                    outfile.write(f"{file_path}:\n{code}\n\n")
                    files_combined += 1

    print(f"\nAll code files have been combined into {output_file}")
    print(f"Total files combined: {files_combined}")

if __name__ == '__main__':
    print("\nWelcome to the Code Combiner Tool!")
    print("This tool combines all readable code files in a directory and its subdirectories into a single output file.\n")

    parser = argparse.ArgumentParser(description="Combine code files from a directory into a single file.")
    parser.add_argument('-i', '--input', default='./', help="Input directory to search for code files (default: current directory)")
    parser.add_argument('-o', '--output', default='combined_output.txt', help="Name of the output file (default: combined_output.txt)")
    parser.add_argument('-e', '--extensions', nargs='+', default=['.json', '.ts', '.txt', '.js', '.html', '.css', '.py', '.prisma', '.tsx', '.cfg'],
                        help="List of file extensions to include (default: common readable types)")

    args = parser.parse_args()
    
    combine_code_files(args.input, args.output, args.extensions)
