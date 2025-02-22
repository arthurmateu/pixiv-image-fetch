import os
import re
import argparse
import webbrowser

# Arguments
parser = argparse.ArgumentParser(prog="pixiv-link-fetch", description="Returns original pixiv links given files with a pixiv filename inside a directory")
parser.add_argument(
    "-O", "--output",
    default="output.txt",
    help=".txt output filename (default: 'output.txt')")
parser.add_argument(
    "directory",
    help="Directory to analyze")
parser.add_argument(
    "-a", "--auto",
    default=False,
    help="Prints out progress, pixiv links and opens them automatically (disabled by default)",
    action=argparse.BooleanOptionalAction,
)
parser.add_argument(
    "--show",
    default=False,
    help="Outputs pixiv links to stdout (disabled by default)",
    action=argparse.BooleanOptionalAction,
)
parser.add_argument(
    "--progress",
    default=False,
    help="Shows progress (disabled by default)",
    action=argparse.BooleanOptionalAction,
)
parser.add_argument(
    "-L", "--limit",
    default=5,
    help="Throttles how many links are opened by default by the `--auto` argument (default=5)"
)
args = parser.parse_args()


# Assigning arguments to variables
directory = args.directory
output_file = args.output if args.output[-4:] == '.txt' else args.output + '.txt'
auto = args.auto
show_stdout = args.show or args.auto
progress = args.progress or args.auto
limit = int(args.limit)



# Relevant functions
def progress(message):
    if progress:
        print(message)



# Global variables
base_link = "https://www.pixiv.net/en/artworks/"
links = set()
cnt = 0
link_quantity = 0



# Actual script begins here
progress("# Fetching files with pixiv filenames in directories...")

for _, _, files in os.walk(directory):
    for file in files:
        # if "_p<num>." in file. creates a group for the code
        match = re.search(r'(\d+)_p\d+\.', file)
        if match:
            code = match.group(1)
            link = base_link + code
            links.add(link)

links = list(links)
link_quantity = len(links)

progress("# Creating an output file with original pixiv links...")

with open(output_file, 'w') as file:
    for link in links:
        file.write(link + "\n")


if show_stdout:
    print("# Pixiv links:")

    for link in links:
        print(f"\033[F\r\033[K[{cnt+1}] - {link}", end="\n\n")

        if auto:
            webbrowser.open_new_tab(link)
            cnt += 1

            if cnt % limit == 0 and cnt < link_quantity:
                pause = input("\033[F\r\033[KContinue? [Y/n] - ").upper()
                if pause and pause[0] == 'N':
                    print(f"\033[F\r\033[K^ Last accessed - visited {cnt} links ^", end="\n\n")
                    auto = False

    print(f"\033[F\r\033[K", end="") # Clean up last empty line
