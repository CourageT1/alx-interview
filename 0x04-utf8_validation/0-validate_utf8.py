#!/usr/bin/python3
"""Write a method that determines if a given data set represents a
valid UTF-8 encoding.
Prototype: def validUTF8(data)
Return: True if data is a valid UTF-8 encoding, else return False
A character in UTF-8 can be 1 to 4 bytes long
The data set can contain multiple characters
The data will be represented by a list of integers
Each integer represents 1 byte of data, therefore you only need
to handle the 8 least significant bits of each integer"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    """
    num_bytes = 0

    for byte in data:
        # Check if the current byte is a leading byte
        if num_bytes == 0:
            if (byte >> 7) == 0:
                # 1-byte character
                continue
            elif (byte >> 5) == 0b110:
                # 2-byte character
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                # 3-byte character
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                # 4-byte character
                num_bytes = 3
            else:
                # Invalid leading byte
                return False
        else:
            # Check if the current byte is a continuation byte
            if (byte >> 6) != 0b10:
                # Invalid continuation byte
                return False

            num_bytes -= 1

    return num_bytes == 0
