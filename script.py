import os
import re
import argparse

# create args
parser = argparse.ArgumentParser(prog="plink", description="Gives pixiv link given a pixiv filename")
parser.add_argument(
    "-O", "--output",
    default="output.txt",
    help=".txt output filename (default: 'output.txt')")
parser.add_argument(
    "directory",
    help="Directory to analyze")
args = parser.parse_args()


# create variables
directory = args.directory
output_file = args.output if args.output[-4:] == '.txt' else args.output + '.txt'
links = []

for _, _, files in os.walk(directory):
    for file in files:
        # if "_p<num>." in file. creates a group for the code
        match = re.search(r'(\d+)_p\d+\.', file)
        if match:
            code = match.group(1)
            link = "https://www.pixiv.net/en/artworks/" + code
            links.append(link)


# make output file
with open(output_file, 'w') as file:
    for link in links:
        file.write(link + "\n")
