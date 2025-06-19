regex_pattern = r"^M{0,3}(CM)?(C?D)?C{0,3}(XC)?(X?L)?X{0,3}(IX)?(I?V)?I{0,3}$"	# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input(0*"Type a ROMAN NUMERAL number: ")))))
