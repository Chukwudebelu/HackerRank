#!/bin/python3
regex_pattern = r"\D"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))
