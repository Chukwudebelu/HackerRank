#!/bin/python3

Regex_start, Regex_end = (r'^', r'$')
_1st_char = r'([a-z])'           # lowercase letter
_2nd_char = r'(\w)'              # word character
_3rd_char = r'(\s)'              # whitespace character
_4th_char = r'(\W)'              # non word character
_5th_char = r'(\d)'              # digit
_6th_char = r'(\D)'              # non digit
_7th_char = r'([A-Z])'           # uppercase letter
_8th_char = r'([a-zA-Z])'        # letter
_9th_char = r'([aeiouAEIOU])'    # vowel
_10th_char = r'(\S)'             # non whitespace character
_11th_char = r'\1'               # same as 1st character
_12th_char = r'\2'               # same as 2nd character
_13th_char = r'\3'               # same as 3rd character
_14th_char = r'\4'               # same as 4th character
_15th_char = r'\5'               # same as 5th character
_16th_char = r'\6'               # same as 6th character
_17th_char = r'\7'               # same as 7th character
_18th_char = r'\8'               # same as 8th character
_19th_char = r'\9'               # same as 9th character
_20th_char = r'\10'              # same as 10th character

Regex_Pattern = rF"{Regex_start}{_1st_char}{_2nd_char}{_3rd_char}{_4th_char}{_5th_char}{_6th_char}{_7th_char}{_8th_char}{_9th_char}{_10th_char}{_11th_char}{_12th_char}{_13th_char}{_14th_char}{_15th_char}{_16th_char}{_17th_char}{_18th_char}{_19th_char}{_20th_char}{Regex_end}"

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
