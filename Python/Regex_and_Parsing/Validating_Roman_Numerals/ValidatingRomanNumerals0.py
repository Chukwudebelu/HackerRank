#!/bin/python3
regex_pattern = r"^(M{0,3})(C{0,3}|CD|D|DC|DCC|DCCC|CM)(X{0,3}|XL|L|LX|LXX|LXXX|XC)(I{0,3}|IV|V|VI|VII|VIII|IX)$"	# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))
