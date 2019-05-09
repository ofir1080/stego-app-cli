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
            if bit_counter == msg_length:
                # if all bits needed already extracted
                return bit_list
            bit_list = np.append(bit_list, str(carrier.mat[row][col][2]))
            bit_counter += 1


def convert_bits_to_txt(bit_list):
    char_list = np.array([])
    for i in range(0, bit_list.size, 8):
        # iterates every 8th bit
        byte = int(''.join(bit_list[i:i + 8]), 2)   # converts every 8 bits to base-2 number
        char_list = np.append(char_list, chr(byte)) # convert byte to char using ASCII and appends to list of chars
    return ''.join(char_list)
