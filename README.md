# SafeText
Script to remove homoglyphs and zero-width characters to allow for safe distribution of documents from anonymous sources.
This script will also search for language that may indicate the author's location. 
This is a work in progress.

## Usage

To use SafeText, call:
```shell
python safetext.py inputfile
```
Example output is:
```shell
λ python safetext.py TestFile.txt
[*] Cleaning TestFile.txt to TestFile.txt.safe ...
FOUND a SPACE ON LINE # 1
[!] WARNING - Use of spelling (colour) that identifies country on line 2
```
SafeText will output to infile.safe. 
