#!/bin/python3
# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

print((m := re.search(r"([a-zA-Z0-9])\1", input())) and m.group(1) or -1)
