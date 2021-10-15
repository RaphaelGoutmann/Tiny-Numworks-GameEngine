# img2array.py

import sys # argv

import numpy as np
from PIL import Image

def usage():
    print("usage: python3 Image2Array [image]")

def main():

    if len(sys.argv) != 2:
        usage()
        exit()

    img = Image.open(sys.argv[1]).convert("RGB")
    array = np.array(img)

    output = open("output.py", 'w')

    # writing
    np.set_printoptions(threshold=np.inf)
    output.write( np.array_repr(array).replace("\n", "").replace(" ", "") )

main()