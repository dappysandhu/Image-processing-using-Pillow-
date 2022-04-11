from PIL import Image, ImageFilter

before = Image.open("trees.bmp")
after = before.filter(ImageFilter.BoxBlur(5))
after.save("out.bmp")