from pyzbar import pyzbar
import argparse
import cv2

ap = argparse.ArgumentParser()

ap.add_argument("-i",  "--image", required=True,
                             help="path to inpt image")

arg = vars(ap.parse_args())

# load the image to memory
image = cv2.imread(arg["image"])

#decode the bars in image
barcodes = pyzbar.decode(image)

for barcode in barcodes:

    (x,y,w,h) = barcode.rect
    cv2.rectangle(image, (x,y), (x+w, y+h), (0,0,225), 2)

    barcodeData = barcode.data.decode("utf-8")
    barcodeType = barcode.type

    text = "{} ({})".format(barcodeData, barcodeType)
    cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 0.5,
                (0, 0, 225), 2)

    print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))

cv2.imshow("Img", image)
cv2.waitKey(0)
