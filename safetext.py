# SafeText
# This script takes an input of a text file, and removes any characters that could be unique identifiers that would
# reveal an otherwise confidential source.
# Inspiration https://www.zachaysan.com/writing/2017-12-30-zero-width-characters
# David Jacobson

import argparse
from characters_safetext import HOMOGLYPHS, ZERO_WIDTH_CHARS


# These are words that could fingerprint an author's location
# Information taken from https://en.oxforddictionaries.com/spelling/british-and-spelling
COUNTRY_SMELLS = (  # Expand this as well
    "centre", "fibre", "litre", "theatre", "colour", "flavour", "humour", "labour", "neighbour", "apologise",
    "organise", "recognise", "analyse", "breathalyse", "paralyse", "travelled", "travelling", "traveller", "paediatric",
    "oestrogen", "manoeuvre", "leukaemia", "defence", "licence", "offence", "pretence", "analogue", "catalogue",
    "dialogue", "grey", "tonne", "honour", "cancelled", "jewellery", "mould", "cheque", "pyjamas",
)

parser = argparse.ArgumentParser(description="Clean a text file of any identifying Unicode characters")
parser.add_argument('input', metavar='I', help='File to be cleaned')
args = parser.parse_args()
out_file_name = args.input + ".safe"
UNDERLINE_START = '\033[4m'
UNDERLINE_END = '\033[0m'
print("[*] Cleaning {} to {} ...".format(args.input, out_file_name))
out_file = open(out_file_name, mode="w", encoding="UTF-8")
with open(args.input, mode="r", encoding="UTF-8") as in_file:  # File to process
    lines = in_file.readlines()  # Read the lines into memory
    for index, line in enumerate(lines):  # Use enum so we can keep track of the lines
        line_to_display = line
        for character in ZERO_WIDTH_CHARS:  # Checking starts here
            if ZERO_WIDTH_CHARS[character] in line:
                print("[!] FOUND a {} ON LINE # {}".format(character, index+1))  # +1 so it's human readable
                line = line.replace(ZERO_WIDTH_CHARS[character], "")
        for character in HOMOGLYPHS:
            if HOMOGLYPHS[character] in line:
                print("[!] FOUND HOMOGLYPHIC CHARACTER {} ON LINE {}".format(character, index+1))
                print(line.replace(HOMOGLYPHS[character], UNDERLINE_START + HOMOGLYPHS[character] + UNDERLINE_END))


        for word in COUNTRY_SMELLS:
            if word in line.lower():  # Normalize
                print("[!] WARNING - Use of spelling ({}) that identifies country on line {}".format(word, index+1))

        lines[index] = line  # Update
for line in lines:
    out_file.write(line)
out_file.close()
print("[*] Output file closed")
