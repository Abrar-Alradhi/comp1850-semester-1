
from image import Image
class LookupTable:
    def __init__(self, mapping):
        self.mapping = mapping
    def display(self):
        for value in range(256):
            print(f"{value} ->{self.mapping[value]}")

    def apply(self,image):
        result = image.copy()
        for i in range(image.width * image.height):
            result[i] = self.mapping[image[i]]
        return result

    
    def apply_in_place(self, image):
        for i in range(image.width * image.height):
            image[i] = self.mapping[image[i]]
        return image
 

img = Image.read("plus.pgm")
lut = LookupTable([255 -x for x in range(256)])

result = lut.apply(img)
result.write_pgm("inverted.pgm")
