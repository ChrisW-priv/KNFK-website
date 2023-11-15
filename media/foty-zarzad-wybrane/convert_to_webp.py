from PIL import Image

def convert(name):
    img = Image.open(name + ".JPG")
    img = img.rotate(90, Image.NEAREST, expand = 1)
    basewidth= 250
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.Resampling.LANCZOS)
    img.save(name + ".webp")

convert("krzysztof")
convert("wiktoria")
convert("maciek")
convert("kuba")
