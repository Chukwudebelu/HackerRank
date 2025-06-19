#!/bin/python3
import re


if __name__ == "__main__":
    regex_start, regex_end = ('^', '$')
    _1s = "((IX)?|VIII|VII|VI|V|IV|III|II|I)"    # Units
    _10s = "((XC)?|LXXX|LXX|LX|L|XL|XXX|XX|X)"    # Tens
    _100s = "((CM)?|DCCC|DCC|DC|D|CD|CCC|CC|C)"    # Hundreds
    _1000s = "((MMM|MM|M)?)"                        # Thousands
    
    regex_pattern = rF"{regex_start}{_1000s}{_100s}{_10s}{_1s}{regex_end}"    # Do not delete 'r'.
    
    print(str(bool(re.match(regex_pattern, input().strip(None)))))
