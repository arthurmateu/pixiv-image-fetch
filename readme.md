# Plink
Plink is a script that generates Pixiv links from a file with a Pixiv filename. It also checks for files in subdirectories.

There is also `plinker.py`, that automatically opens up each link generated.

# Usage and options
## Plink
```
python script.py [OPTIONS] directory
```
### General options:
```
  -h, --help                        show this help message and exit
  -O OUTPUT, --output OUTPUT        .txt output filename (default: 'output.txt')
```

## Plinker
```
python plinker.py [OPTIONS] input
```
### General options:
```
  -h, --help                        show this help message and exit
  -L LIMIT, --limit LIMIT           throttle to how many links you want opened at once
```
