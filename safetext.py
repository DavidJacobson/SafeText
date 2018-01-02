# SafeText
# This script takes an input of a text file, and removes any characters that could be unique identifiers that would
# reveal an otherwise confidential source.
# Inspiration https://www.zachaysan.com/writing/2017-12-30-zero-width-characters
# David Jacobson

import argparse

# We need to remove Zero Width Characters, Control Characters, and homoglyphs
ZERO_WIDTH_CHARS = {
    "SPACE": u'\u200b',
    "NON-JOINER CODE POINT": u'\u200c',
    "JOINER CODE POINT": u'\u200d',
    "NO BREAK SPACE CODE POINT": u'\uFEFF',
}

# A list of letters that have identical counterparts from other character sets
# Please note that these are stored with reference to their english counterparts, i.e. CYRILLIC_b may not be the
# second letter of the Cyrillic alphabet.
# List built from https://en.wikipedia.org/wiki/IDN_homograph_attack
HOMOGLYPHS = {  # To verify these are Cyrillic characters, enter them into Google with autocomplete
    # These characters are used in Russian, Belarusian, Ukrainian, Bulgarian, Serbian, Bosnian, Croatian and more
    # This character set is the most common used in homoglyph fingerprinting as it has the most characters that are
    # visually similar to their latin counterparts
    "CYRILLIC_a":  u"а",
    "CYRILLIC_small_b": u"ь",
    "CYRILLIC_large_b": u"Ъ",
    "CYRILLIC_c": u"с",
    "CYRILLIC_d": u"ԁ",
    "CYRILLIC_e": u"е",
    "CYRILLIC_small_h": u"һ",
    "CYRILLIC_large_h": u"Һ",
    "CYRILLIC_i": u"і",
    "CYRILLIC_j": u"ј",
    "CYRILLIC_o": u"о",
    "CYRILLIC_p": u"р",
    "CYRILLIC_s": u"ѕ",
    "CYRILLIC_small_v": u"ѵ",
    "CYRILLIC_large_v": u"Ѵ",
    "CYRILLIC_x": u"х",
    "CYRILLIC_y": u"у",

    "CYRILLIC_A": u"А",
    "CYRILLIC_small_B": u"в",
    "CYRILLIC_large_B": u"В",
    "CYRILLIC_small_C": u"с",
    "CYRILLIC_large_C": u"С",
    "CYRILLIC_E": u"Е",
    "CYRILLIC_small_F": u"ғ",
    "CYRILLIC_large_F": u"Ғ",
    "CYRILLIC_small_G": u"ԍ",
    "CYRILLIC_large_G": u"Ԍ",
    "CYRILLIC_small_H": u"н",
    "CYRILLIC_large_H": u"Н",
    "CYRILLIC_I": u"І",
    "CYRILLIC_J": u"Ј",
    "CYRILLIC_small_K": u"к",
    "CYRILLIC_large_K": u"К",
    "CYRILLIC_small_M": u"м",
    "CYRILLIC_large_M": u"М",
    "CYRILLIC_small_O": u"о",
    "CYRILLIC_large_O": u"О",
    "CYRILLIC_P": u"Р",
    "CYRILLIC_S": u"Ѕ",
    "CYRILLIC_small_T": u"т",
    "CYRILLIC_large_T": u"Т",
    "CYRILLIC_X": u"Х",
    "CYRILLIC_Y": u"У",


# Todo expand this portion
}

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
print("[*] Cleaning {} to {} ...".format(args.input, out_file_name))
out_file = open(out_file_name, mode="w", encoding="UTF-8")
with open(args.input, mode="r", encoding="UTF-8") as in_file:  # File to process
    lines = in_file.readlines()  # Read the lines into memory
    for index, line in enumerate(lines):  # Use enum so we can keep track of the lines
        for character in ZERO_WIDTH_CHARS:  # Checking starts here
            if ZERO_WIDTH_CHARS[character] in line:
                print("[!] FOUND a {} ON LINE # {}".format(character, index+1))  # +1 so it's human readable
                line = line.replace(ZERO_WIDTH_CHARS[character], "")
        for character in HOMOGLYPHS:
            if HOMOGLYPHS[character] in line:
                print("[!] FOUND HOMOGLYPHIC CHARACTER {} ON LINE {}".format(character, index+1))
        for word in COUNTRY_SMELLS:
            if word in line.lower():  # Normalize
                print("[!] WARNING - Use of spelling ({}) that identifies country on line {}".format(word, index+1))

        lines[index] = line  # Update
for line in lines:
    out_file.write(line)
out_file.close()
print("[*] Output file closed")
