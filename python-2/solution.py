#!/usr/bin/env python2
# solve.py

'''
1.) Take the RGB value of every pixel in one image. (Start at (0,0). Move down to (0,300). Go to (1,0). Move to (1,300). And so on. Read the files in numerical order.)
2.) Add all of the R values, G values, and B values in each image.
3.) Take these sums and convert them into strings. Take the MD5 hash of each string.
4.) Concatenate these MD5 hashes into one string.
5.) Take the MD5 hash of the new string.
6.) Do this for every image and concatenate the final MD5 hashes into one string.
7.) Take the MD5 of this string to get the flag.
'''


import hashlib
import PIL.Image


def md5str(arg):
    return hashlib.md5(str(arg)).hexdigest()


def main():
    filename = 'PIL/pixels{}.png'
    final_hashes = ''

    for n in range(10):
        img = PIL.Image.open(filename.format(n))
        img.convert('RGB')
        data, (width, height) = img.getdata(), img.size
        r_sum, g_sum, b_sum = 0, 0, 0
        
        for r, g, b in data:
            r_sum += r
            g_sum += g
            b_sum += b
        else:
            sum_hashes = md5str(r_sum) + md5str(g_sum) + md5str(b_sum)
            final_hashes += md5str(sum_hashes)
    else:
        print 'Flag:', md5str(final_hashes)


if __name__ == '__main__':
    main()
