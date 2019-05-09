#
# def convert_str_to_bin(msg):
#     binary_list = [bin(ord(c))[2:] for c in msg]
#     return ''.join(binary_list)


def inject(carrier, msg):
    bit_counter = 0
    for row in range(carrier.height):
        for col in range(carrier.width):
            if bit_counter >= msg.size:
                # run as long as there are bits to inject
                return
            print(carrier.mat[row][col])
            carrier.mat[row][col] = set_pixel(carrier.mat[row][col], msg.bit_list[bit_counter:bit_counter + 3])
            bit_counter += 3


def set_pixel(pixel, bits):
    # new_pixel = (pixel[:bits.size] & 0b01111111) | (bits << 7)    # uncomment to set MSBs
    new_pixel = (pixel[:bits.size] & 0b11111110) | bits
    return new_pixel
