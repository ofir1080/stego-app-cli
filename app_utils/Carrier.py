import os
from PIL import Image
import numpy as np


class Carrier:

    def __init__(self, image_path):
        self.name = os.path.basename(image_path)
        image = Image.open(image_path)
        self.mat = np.array(image)[..., :3]
        # print(self.mat.shape)
        image.close()
        self.height = self.mat.shape[0]
        self.width = self.mat.shape[1]

    def create_image(self):
        carrier_image = Image.new('RGB', (self.width, self.height))
        for row in range(self.height):
            for col in range(self.width):
                # print(row, col)
                carrier_image.putpixel((col, row), tuple(self.mat[row][col]))
        carrier_image.save('images/OUT_' + self.name)
        carrier_image.show()
