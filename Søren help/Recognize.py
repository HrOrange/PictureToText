from PIL import Image
from os import listdir
from os.path import isfile, join
import time

mypath = "C:/Users/nicol/Desktop/Søren help/pics"
files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
width, height = Image.open(mypath + "/" + files[0]).size

mypathalpha = "C:/Users/nicol/Desktop/Søren help/Alphas"
alphas = [f for f in listdir(mypathalpha) if isfile(join(mypathalpha, f)) and f[-6:-4] == "_3"]
alp = [Image.open(mypathalpha + "/" + f).load() for f in alphas]
widthA, heightA = Image.open(mypathalpha + "/" + alphas[0]).size

punktumWhite = 680
whiteValue = 500
whiteValue2 = 400

for name in files:
    img = Image.open(mypath + "/" + name)
    pix = img.load()

    #check om det er et kommatal
    est = 0
    for x in range(0, 4):
        for y in range(4):
            #print(pix[48 + x, 24 + y])
            est += pix[48 + x, 24 + y][0] + pix[48 + x, 24 + y][1] + pix[48 + x, 24 + y][2]

    #print(est / 16)
    if(est / 16 > punktumWhite):
        #print("Der er et punktum") #derfor ved vi nu at tallet må være under 100

        tal = 0.0

        #første karakter
        karakter = 0
        korrekt = 0
        offset = [14, 8]
        for z in range(len(alp)):
            iden = 0
            whiteSpaces = 0
            for x in range(widthA):
                for y in range(heightA):
                    val = pix[offset[0] + x, offset[1] + y] #get pic color values
                    valAlpha = alp[z][x, y] #get alpha color values

                    if(valAlpha[0] + valAlpha[1] + valAlpha[2] > whiteValue):
                        whiteSpaces += 1

                    if(val[0] + val[1] + val[2] > whiteValue and
                       valAlpha[0] + valAlpha[1] + valAlpha[2] > whiteValue):
                        iden += 1
            if(iden / whiteSpaces > korrekt):
                korrekt = iden / whiteSpaces
                karakter = z
        tal += karakter * 10

        #anden karakter
        karakter = 0
        korrekt = 0
        offset = [30, 8]
        for z in range(len(alp)):
            iden = 0
            whiteSpaces = 0
            for x in range(widthA):
                for y in range(heightA):
                    val = pix[offset[0] + x, offset[1] + y] #get pic color values
                    valAlpha = alp[z][x, y] #get alpha color values

                    if(valAlpha[0] + valAlpha[1] + valAlpha[2] > whiteValue):
                        whiteSpaces += 1

                    if(val[0] + val[1] + val[2] > whiteValue and
                       valAlpha[0] + valAlpha[1] + valAlpha[2] > whiteValue):
                        iden += 1
            #print(str(iden / whiteSpaces))
            if(iden / whiteSpaces > korrekt):
                korrekt = iden / whiteSpaces
                karakter = z
        tal += karakter
        #tal += "."

        #tredje karakter
        karakter = 0
        korrekt = 0
        offset = [55, 8]
        for z in range(len(alp)):
            iden = 0
            whiteSpaces = 0
            for x in range(widthA):
                for y in range(heightA):
                    val = pix[offset[0] + x, offset[1] + y] #get pic color values
                    valAlpha = alp[z][x, y] #get alpha color values

                    if(valAlpha[0] + valAlpha[1] + valAlpha[2] > whiteValue):
                        whiteSpaces += 1

                    if(val[0] + val[1] + val[2] > whiteValue and
                       valAlpha[0] + valAlpha[1] + valAlpha[2] > whiteValue):
                        iden += 1
            #print(str(iden / whiteSpaces))
            if(iden / whiteSpaces > korrekt):
                korrekt = iden / whiteSpaces
                karakter = z
        tal += karakter / 10

        print(tal)
    else: #derfor ved vi nu at tallet må være over eller lig med 100
        tal = 0

        #1. karakter
        karakter = 0
        korrekt = 0
        offset = [14, 8]
        for z in range(len(alp)):
            iden = 0
            whiteSpaces = 0
            for x in range(widthA):
                for y in range(heightA):
                    val = pix[offset[0] + x, offset[1] + y] #get pic color values
                    valAlpha = alp[z][x, y] #get alpha color values

                    if(valAlpha[0] + valAlpha[1] + valAlpha[2] > whiteValue):
                        whiteSpaces += 1

                    if(val[0] + val[1] + val[2] > whiteValue and
                       valAlpha[0] + valAlpha[1] + valAlpha[2] > whiteValue):
                        iden += 1
            if(iden / whiteSpaces > korrekt):
                korrekt = iden / whiteSpaces
                karakter = z
        tal += karakter * 100

        #2. karakter
        karakter = 0
        korrekt = 0
        offset = [30, 8]
        for z in range(len(alp)):
            iden = 0
            whiteSpaces = 0
            for x in range(widthA):
                for y in range(heightA):
                    val = pix[offset[0] + x, offset[1] + y] #get pic color values
                    valAlpha = alp[z][x, y] #get alpha color values

                    if(valAlpha[0] + valAlpha[1] + valAlpha[2] > whiteValue):
                        whiteSpaces += 1

                    if(val[0] + val[1] + val[2] > whiteValue and
                       valAlpha[0] + valAlpha[1] + valAlpha[2] > whiteValue):
                        iden += 1
            if(iden / whiteSpaces > korrekt):
                korrekt = iden / whiteSpaces
                karakter = z
        tal += karakter * 10

        #3. karakter
        karakter = 0
        korrekt = 0
        offset = [46, 8]
        for z in range(len(alp)):
            iden = 0
            whiteSpaces = 0
            for x in range(widthA):
                for y in range(heightA):
                    val = pix[offset[0] + x, offset[1] + y] #get pic color values
                    valAlpha = alp[z][x, y] #get alpha color values

                    if(valAlpha[0] + valAlpha[1] + valAlpha[2] > whiteValue):
                        whiteSpaces += 1

                    if(val[0] + val[1] + val[2] > whiteValue and
                       valAlpha[0] + valAlpha[1] + valAlpha[2] > whiteValue):
                        iden += 1
            if(iden / whiteSpaces > korrekt):
                korrekt = iden / whiteSpaces
                karakter = z
        tal += karakter

        print(tal)
