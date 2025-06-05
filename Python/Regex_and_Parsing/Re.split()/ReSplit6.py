#!/bin/python3
# '\W' matches all NON-WORD characters
regex_pattern = r"\W"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))
