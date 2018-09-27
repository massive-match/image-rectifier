from PIL import Image

def proccess(iName, oName):
    img = Image.open(iName, 'r')
    to700(img, oName + "_700.jpg")
    to1500(img, oName + "_1500.jpg")
    return "OK"

def proccess700(i_name, o_name):
    img = Image.open(i_name, 'r')
    to1500(img, o_name)
    return "OK"

def proccess1500(i_name, o_name):
    img = Image.open(i_name, 'r')
    to1500(img, o_name)
    return "OK"

def resize(img, max_size):
    width, height = img.size
    if width >= height:
        factor = height / width
        r_heigth = int(max_size * factor)
        return img.resize((max_size, r_heigth), Image.ANTIALIAS)
    else:
        factor = width / height
        r_width = int(max_size * factor)
        return img.resize((r_width, max_size), Image.ANTIALIAS)

def to700(img, name):
    img = resize(img, 610)
    img_w, img_h = img.size
    background = Image.new('RGB', (700, 700), (255, 255, 255))
    bg_w, bg_h = background.size
    offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
    background.paste(img, offset)
    background.save(name)

def to1500(img, name):
    img = resize(img, 1410)
    img_w, img_h = img.size
    background = Image.new('RGB', (1500, 1500), (255, 255, 255))
    bg_w, bg_h = background.size
    offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
    background.paste(img, offset)
    background.save(name)