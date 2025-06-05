#!/bin/python3
# '\D' matches all NON-DIGIT characters
regex_pattern = r"\D"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))
