#!/usr/bin/python3
""" A utf-8 validation module """


def validUTF8(data):
    """ a method that determines if a given data
        set represents a valid UTF-8 encoding
    """
    for byte in data:
        bitchar = format(byte, '08b')
        if bitchar.startswith('0'):
            continue
        elif bitchar.startswith('110'):
            continue
        elif bitchar.startswith('1110'):
            continue
        elif bitchar.startswith('1110'):
            continue
        else:
            return False
    return True
