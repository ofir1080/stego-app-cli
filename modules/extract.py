"""
the module extract the message from a given image (of type carrier) and
length of the message in bits (k * 8 where k is the number of characters.
"""
import numpy as np


def extract_msg(carrier, length):
    extracted_bits = extract_LSB(carrier, length)
    msg = convert_bits_to_txt(extracted_bits)
    return msg


def extract_LSB(carrier, msg_length):
    """

    :param carrier: obj of type Carrier representing the carrier image
    :param msg_length: the length of the message in bits (where each character is of size 8)
    :return: a list of bits of the message
    """
    bit_list = np.array([])
    bit_counter = 0
    for row in range(carrier.height):
        for col in range(carrier.width):
            if bit_counter >= msg_length:
                # if all bits needed already extracted
                return bit_list
            bit_list = np.append(bit_list, extract_LSB_from_RGB(carrier.mat[row][col], min(3, msg_length - bit_counter)))
            bit_counter += 3


def extract_LSB_from_RGB(pixel, bits_in_pixel):
    """
    return a list of the required LSBs (max 3)
    :param pixel: list of size 3 (RGB type)
    :param bits_in_pixel: how many LSbits need to be extracted (1, 2 or 3)
    :return: list of max-3 size containing 0s/1s (bits of the injected message)
    """
    bits = []
    for i in range(bits_in_pixel):
        bits.append(bin(pixel[i])[-1])
    return bits


def convert_bits_to_txt(bit_list):
    """

    :param bit_list: list of chars ('0' of '1') of size k*8 representing bytes of ascii chars
    :return: the extracted text
    """
    char_list = np.array([])
    for i in range(0, bit_list.size, 8):
        # iterates every 8th bit
        byte = int(''.join(bit_list[i:i + 8]), 2)   # converts every 8 bits to base-2 number
        char_list = np.append(char_list, chr(byte)) # convert byte to char using ASCII and appends to list of chars
    return ''.join(char_list)

