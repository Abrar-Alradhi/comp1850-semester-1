from image import Image
lut = [255 -x for x in range(256)]
img = Image.read("some_image.pgm")
new_img = lut.apply(img)
new_img.write_pgm("inverted.pgm")