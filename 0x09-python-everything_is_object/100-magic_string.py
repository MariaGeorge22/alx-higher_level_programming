#!/usr/bin/python3
def magic_string():
    magic_string.calls = getattr(magic_string, 'calls', 0) + 1
    return ", ".join(list("BestSchool" for i in range(magic_string.calls)))
