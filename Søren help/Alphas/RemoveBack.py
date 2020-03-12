from PIL import Image, ImageOps
from os import listdir
from os.path import isfile, join

mypath = "C:/Users/nicol/Desktop/Søren help"
files = [f for f in listdir(mypath) if isfile(join(mypath, f)) and f[-6:-4] != "_2" and f[-6:-4] != "_3"]
width, height = Image.open(files[0]).size

for name in files:
    if(name[-3:] == "png"):
        img = Image.open(name)
        pix = img.load()
        for x in range(img.size[0]):
            for y in range(img.size[1]):
                if(pix[x, y][0] + pix[x, y][1] + pix[x, y][2] < 500):
                    pix[x, y] = (0, 0, 0)
                else:
                    pix[x, y] = (255, 255, 255)
        #img2 = ImageOps.fit(img, (width * 10, height * 10), Image.ANTIALIAS)
        img.save(name[0:-4] + "_3" + ".png")
