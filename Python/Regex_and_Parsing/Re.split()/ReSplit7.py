#!/bin/python3
# Without using Regex Module

def re_split(regex_pattern) -> None:
    if "," in regex_pattern:
        A1 = regex_pattern.split(",")
        A2 = []
        for string in A1:
            A2 += string.split(".")

    elif "." in regex_pattern:
        A1 = regex_pattern.split(".")
        A2 = []
        for string in A1:
            A2 += string.split(",")
  
    print("\n".join(A2))
