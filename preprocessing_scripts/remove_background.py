import os

from PIL import Image

size_1 = 700, 700
size_2 = 512, 512


def remove_background_noise(src, dst):
    dirs = os.listdir(src)
    for img2 in dirs:
        if not (os.path.isfile(src + img2)) or (not (img2.endswith('.jpeg'))):
            continue
        img = Image.open(src + img2)
        img = img.resize(size_1, Image.ANTIALIAS)
        wd, ht = img.size
        pix = img.load()
        for i in range(0, ht):
            for j in range(0, wd):
                if pix[j, i] > (15, 15, 15):
                    break
            if pix[j, i] > (15, 15, 15):
                break
        ht1 = i
        i = ht - 1
        while i > 0:
            for j in range(0, wd):
                if pix[j, i] > (15, 15, 15):
                    break
            if pix[j, i] > (15, 15, 15):
                break
            i = i - 1
        ht2 = i

        for i in range(0, wd):
            for j in range(0, ht):
                if pix[i, j] > (15, 15, 15):
                    break
            if pix[i, j] > (15, 15, 15):
                break
        wd1 = i
        i = wd - 1
        while i > 0:
            for j in range(0, ht):
                if pix[i, j] > (15, 15, 15):
                    break
            if pix[i, j] > (15, 15, 15):
                break
            i = i - 1
        wd2 = i
        img3 = img.crop((wd1, ht1, wd2, ht2))
        img3 = img3.resize(size_2, Image.ANTIALIAS)
        img3.save(dst + img2)


remove_background_noise(src='/content/train_data_original/', dst='/content/cropped_512_512/')
