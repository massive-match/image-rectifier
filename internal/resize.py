from PIL import Image

def resize(iName, oName):
    img = Image.open(iName, 'r')
    img = img.resize((300, 450), Image.ANTIALIAS)
    img_w, img_h = img.size
    background = Image.new('RGBA', (700, 700), (255, 255, 255, 255))
    bg_w, bg_h = background.size
    offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
    background.paste(img, offset)
    im = background.convert('RGB')
    im.save(oName)
    return "OK"