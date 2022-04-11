from PIL import Image, ImageFilter

before = Image.open("trees.bmp")
after = before.filter(ImageFilter.FIND_EDGES)
after.save("edges.bmp")