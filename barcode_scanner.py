from pyzbar import pyzbar
import argparse
import cv2

ap = argparse.ArgumentParser()

ap.add_argument("-i",  "--image", required=True,
                             help="path to inpt image")

arg - vars(ap.parse_args())

# load the image to memory

image = cv2.imread(arg["image"])

#decode the bars in image
barcodes = pyzbar.decode(image)
