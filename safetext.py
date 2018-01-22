# -- coding: utf-8 --

# SafeText
# This script takes an input of a text file, and removes any characters that could be unique identifiers that would
# reveal an otherwise confidential source.
# Inspiration https://www.zachaysan.com/writing/2017-12-30-zero-width-characters
# David Jacobson

import argparse
import sys
from characters_safetext import HOMOGLYPHS, ZERO_WIDTH_CHARS, NON_STANDARD_SPACES
from unicodedata import normalize


def underline(chars):
    if WIN:
        return "'{}'".format(chars)
    return '\033[4m' + chars + '\033[0m'


def safe_windows_print(s):
        try:
            print(s)
        except UnicodeEncodeError as e:
            for c in s:
                try:
                    print(c, end='')
                except UnicodeEncodeError as d:
                    print('?', end='')


COUNTRY_SMELLS = {
    "BRIT_SPELLS": [],
    "US_SPELLS": [],
}
for SPELL_FILE in ["BRIT_SPELLS", "US_SPELLS"]:
    with open(SPELL_FILE, "r") as WORD_FILE:
        lines = WORD_FILE.readlines()
        for each in lines:
            COUNTRY_SMELLS[SPELL_FILE].append(each.strip())

parser = argparse.ArgumentParser(description="Clean a text file of any identifying Unicode characters")
parser.add_argument('input', metavar='I', help='File to be cleaned')
args = parser.parse_args()
out_file_name = args.input + ".safe"
print("[*] Cleaning {} to {} ...".format(args.input, out_file_name))

# get platform once
WIN = sys.platform == 'win32'


with open(args.input, mode="r", encoding="UTF-8") as in_file:  # File to process
    lines = in_file.readlines()  # Read the lines into memory
    for index, line in enumerate(lines):  # Use enum so we can keep track of the lines
        line_to_display = line  # This will be the line presented to the user, to highlight what characters were hidden
        # print(normalize("NFKC", line))
        for character in ZERO_WIDTH_CHARS:  # Checking starts here
            if ZERO_WIDTH_CHARS[character] in line:
                display_line = True
                print("[!] FOUND a {} ON LINE # {}".format(character, index+1))  # +1 so it's human readable
                line_to_display = line_to_display.replace(ZERO_WIDTH_CHARS[character], "*")
                line = line.replace(ZERO_WIDTH_CHARS[character], "")  # To actually remove
        for letter in HOMOGLYPHS:
            if HOMOGLYPHS[letter] in line:
                display_line = True
                # print(underline(HOMOGLYPHS[character]))
                print("[!] FOUND HOMOGLYPHIC CHARACTER {} ON LINE {}".format(letter, index+1))
                line_to_display = line_to_display.replace(HOMOGLYPHS[letter], underline(HOMOGLYPHS[letter]))
                replacement_char = letter[-1]
                line = line.replace(HOMOGLYPHS[letter], replacement_char)
        for space in NON_STANDARD_SPACES:
            if NON_STANDARD_SPACES[space] in line:
                print("[!] FOUND A NON STANDARD SPACE ON LINE {}".format(index+1))
                line_to_display = line_to_display.replace(NON_STANDARD_SPACES[space], "*")  # Highlight for display
                line = line.replace(NON_STANDARD_SPACES[space], " ")  # Normalize
        if line_to_display != line:  # If the line had to be modified, print it.
            if WIN:
                safe_windows_print(line_to_display.strip())
            else:
                print(line_to_display.strip())

        for SPELLINGS in COUNTRY_SMELLS:
            for word in COUNTRY_SMELLS[SPELLINGS]:
                if word in line.lower():  # Normalize
                    print("[!] WARNING - Use of spelling ({}) that identifies country on line {}".format(word, index+1))
                    print("[*] GUESS OF COUNTRY: {}".format(SPELLINGS.split("_")[0]))

        lines[index] = line  # Update

out_file = open(out_file_name, mode="w", encoding="UTF-8")
for line in lines:
    out_file.write(line)
out_file.close()
print("[*] Output file closed")
