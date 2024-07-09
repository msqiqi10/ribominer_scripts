import re
import sys

def replace_spaces_with_tabs(input_file, output_file):
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                modified_line = re.sub(r'\s+', '\t', line) + '\n'
                outfile.write(modified_line)
        print(f"Processed file saved as: {output_file}")
    except OSError as e:
        print(f"Error: {e}")
        print("Please check your input files!")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python replace_spaces_with_tabs.py <input_file> <output_file>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        replace_spaces_with_tabs(input_file, output_file)