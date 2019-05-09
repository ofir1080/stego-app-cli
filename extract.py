import numpy as np


def extract_msg(carrier, length):
    extracted_bits = extract_LSB(carrier, length)
    msg = convert_bits_to_txt(extracted_bits)
    return msg


def extract_LSB(carrier, msg_length):
    bit_list = np.array([])
    bit_counter = 0
    for row in range(carrier.height):
        for col in range(carrier.width):
            if bit_counter >= msg_length:
                # if all bits needed already extracted
                return bit_list
            bit_list = np.append(bit_list, extract_LSB_from_RGB(carrier.mat[row][col], min(3, msg_length - bit_counter)))
            bit_counter += 3


def convert_bits_to_txt(bit_list):
    char_list = np.array([])
    print(bit_list.size)
    for i in range(0, bit_list.size, 8):
        # iterates every 8th bit
        byte = int(''.join(bit_list[i:i + 8]), 2)   # converts every 8 bits to base-2 number
        char_list = np.append(char_list, chr(byte)) # convert byte to char using ASCII and appends to list of chars
    return ''.join(char_list)


def extract_LSB_from_RGB(pixel, bits_in_pixel):
    bits = []
    for i in range(bits_in_pixel):
        bits.append(bin(pixel[i])[-1])
    return bits
