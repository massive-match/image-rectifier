from PIL import Image

def resize(iName, oName):
    img = Image.open(iName, 'r')
    to700(img, oName)
    to1500(img, oName)
    return "OK"

def to700(img, name):
    img = img.resize((406, 610), Image.ANTIALIAS)
    img_w, img_h = img.size
    background = Image.new('RGB', (700, 700), (255, 255, 255))
    bg_w, bg_h = background.size
    offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
    background.paste(img, offset)
    background.save(name + "_700.jpg")

def to1500(img, name):
    img = img.resize((940, 1410), Image.ANTIALIAS)
    img_w, img_h = img.size
    background = Image.new('RGB', (1500, 1500), (255, 255, 255))
    bg_w, bg_h = background.size
    offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
    background.paste(img, offset)
    background.save(name + "_1500.jpg")