#!/bin/python3

THOUSANDs = 'M{0,3}'
HUNDREDs = '(C[MD]|D{0,1}C{0,3})'
TENs = '(X[CL]|L{0,1}X{0,3})'
ONEs = '(I[VX]|V{0,1}I{0,3})'

regex_pattern = r"^%s%s%s%s$" % (THOUSANDs, HUNDREDs, TENs, ONEs)    # Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input(None)))))
