from pyzbar import pyzbar
import argparse
import cv2

ap = argparse.ArgumentParser()

ap.add_argument("-i",  "--image", required=True,
                             help="path to inpt image")

args - vars(ap.parse_args())
