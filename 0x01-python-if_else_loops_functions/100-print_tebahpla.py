#!/usr/bin/python3
isCapital = False
for a in reversed(range(ord('a'), ord('z') + 1)):
    a = a if not isCapital else a + (ord('A')-ord('a'))
    print("{0}".format(chr(a)), end="")
    isCapital = not isCapital
