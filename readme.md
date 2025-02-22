# pixiv-image-fetch
pixiv-image-fetch is a CLI-tool that fetches original Pixiv links from a file with a Pixiv filename within a directory (and subdirectories).

## Usage and options
### Usage
```
usage: pixiv-link-fetch [-h] [-O OUTPUT] [-a | --auto | --no-auto] [--show | --no-show] [--progress | --no-progress] [-L LIMIT] directory

```
### Options
```
positional arguments:
  directory             Directory to analyze

options:
  -h, --help            show this help message and exit
  -O, --output OUTPUT   .txt output filename (default: 'output.txt')
  -a, --auto, --no-auto
                        Prints out progress, pixiv links and opens them automatically (disabled by default)
  --show, --no-show     Outputs pixiv links to stdout (disabled by default)
  --progress, --no-progress
                        Shows progress (disabled by default)
  -L, --limit LIMIT     Throttles how many links are opened by default by the `--auto` argument (default=5)
```
