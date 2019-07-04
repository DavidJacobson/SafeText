# -- coding: utf-8 --

# This is a file to store all the characters that SafeText will look out for

# Zero width characters are visible when reading, as they take up no space. However, they can be used in fingerprinting.
# Below is a list of Unicode's zero width characters.


ZERO_WIDTH_CHARS = {
    "SPACE": u'\u200b',
    "NON-JOINER CODE POINT": u'\u200c',
    "JOINER CODE POINT": u'\u200d',
    "NO BREAK SPACE CODE POINT": u'\uFEFF',
    "RIGHT LEFT MARK": 	u"\u200F",
    "LEFT RIGHT MARK": 	u"\u200E",

}

NON_STANDARD_SPACES = {  # These are not zero-width, they are visible. However, they are unique, and need to
    # be normalized
    "EN QUAD": u"\u2000",
    "HAIR SPACE": u"\u200A",
    "NARROW NO BREAK SPACE": u"\u202F",
    "MEDIUM MATHEMATICAL SPACE": u"\u205F",
    "EN SPACE": u"\u2002",
    "EM SPACE": u"\u2003",
    "THREE PER EM SPACE": u"\u2004",
    "FOUR PER EM SPACE": u"\u2005",
    "SIX PER EM SPACE": u"\u2006",
    "FIGURE SPACE": u"\u2007",
    "PUNCTUATION SPACE": u"\u2008",
    "THIN SPACE": u"\u2009",
    "<> (IS)": u"\u3000",
}
# A list of letters that have identical counterparts from other character sets.
# Please note that these are stored with reference to their English counterparts, i.e. CYRILLIC_b is not be the
# second letter of the Cyrillic alphabet, rather it is the Cyrillic character that most resembles the letter 'b'.
# List built from https://en.wikipedia.org/wiki/IDN_homograph_attack + manual inspection of characters.
HOMOGLYPHS = {  # To quickly verify that these characters are not Latin, enter them in Google with autocomplete.
    #           The response should be a character set other than Latin.
    #           The characters are organized by: CHARACTER SET _ [UPPER/LOWER] _ LATIN COUNTERPART
    #           EG: GREEK_SMALL_B
    # Cyrillic characters are used in Russian, Belarusian, Ukrainian, Bulgarian, Serbian, Bosnian, Croatian and more.
    # This character set is the most common used in homoglyph fingerprinting as it has the most characters that are
    # visually similar to their Latin counterparts
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


    "CYRILLIC_3": u"З",
    "CYRILLIC_4": u"Ч",
    "CYRILLIC_6": u"б",


    # Greek characters
    # There are Greek characters that are identical to Cyrillic, German, and Serbian
    # however this tool is built around Latin.

    "GREEK_c": u"ϲ",
    "GREEK_i": u"ί",
    "GREEK_o": u"ο",
    "GREEK_p": u"ρ",
    "GREEK_w": u"ω",
    "GREEK_v": u"ν",

    "GREEK_A": u"Α",
    "GREEK_B": u"Β",
    "GREEK_C": u"Ϲ",
    "GREEK_E": u"Ε",
    "GREEK_H": u"Η",
    "GREEK_I": u"Ι",
    "GREEK_J": u"Ϳ",
    "GREEK_small_K": u"Κ",
    "GREEK_large_K": u"κ",
    "GREEK_small_M": u"Μ",
    "GREEK_large_M": u"Ϻ",
    "GREEK_N": u"Ν",
    "GREEK_O": u"Ο",
    "GREEK_T": u"Τ",
    "GREEK_U": u"υ",
    "GREEK_X": u"Χ",
    "GREEK_Y": u"Υ",
    "GREEK_Z": u"Ζ",

    # Armenian characters

    "ARMENIAN_g": u"ց",
    "ARMENIAN_o": u"օ",
    "ARMENIAN_j": u"յ",
    "ARMENIAN_h": u"հ",
    "ARMENIAN_n": u"ո",
    "ARMENIAN_u": u"ս",
    "ARMENIAN_q": u"զ",

    "ARMENIAN_L": u"Լ",
    "ARMENIAN_O": u"Օ",
    "ARMENIAN_U": u"Ս",
    "ARMENIAN_S": u"Տ",

    "ARMENIAN_2": u"Ձ",
    "ARMENIAN_ALT_2": u"շ",
    "ARMENIAN_3": u"Յ",
    "ARMENIAN_4": u"վ",

    # Hebrew Characters

    "HEBREW_i": "וֹ",
    "HEBREW_n": "ח",

    "HEBREW_O": "ס",

    # Script characters

    "SCRIPT_i": u"í",

}
