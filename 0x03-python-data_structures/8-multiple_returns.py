#!/usr/bin/python3
def multiple_returns(sentence):
    str_len, first_char = (0, None)
    if len(sentence) > 0:
        str_len, first_char = (len(sentence), sentence[0])
    return (str_len, first_char)
