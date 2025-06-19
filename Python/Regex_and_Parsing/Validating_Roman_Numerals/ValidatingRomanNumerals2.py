#!/bin/python3
import re


if __name__ == "__main__":
    start = r"^"
    thousands = r"(?P<thousands>M{0,3})"            # 1000s
    hundreds = r"(?P<hundreds>CM|CD|(D?C{0,3}))"    # 100s
    tens = r"(?P<tens>XC|XL|(L?X{0,3}))"            # 10s
    ones = r"(?P<units>IX|IV|(V?I{0,3}))"           # 1s
    end = r"$"
    
    regex_pattern = r"" + start + thousands + hundreds + tens + ones + end     # Do not delete 'r'.
    
    print(bool(re.match(regex_pattern, str(input('')))))
