from pyzbar import pyzbar
import argparse
import cv2
import imutils
from imutils.video import VideoStream
import time
import datetime

ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", type=str, default="barcodes.csv",
                help="path to output CSV file containig barcodes")

args = vars(ap.parse_args())

print("[INFO] video stream starting......")
vs = VideoStream(src=0).start()
time.sleep(2)

csv = open(args["output"], "w")
found = set()

# capturing and porcessing frames
while True:
    frame = vs.read()
    frame = imutils.resize(frame, width=1000)

    barcodes = pyzbar.decode(frame)

    # Decte barcode 
    for barcode in barcodes:
        (x,y,w,h) = barcode.rect
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,225), 2)

        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type

        text = "{} ({})".format(barcodeData, barcodeType)
        cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 0.5,
                    (0, 0, 225), 2)
        if barcodeData not in found:
            csv.write("{},{}\n".format(datetime.now(), barcodeData))
            csv.flush()
            found.add(barcodeData)


    cv2.imshow("Img", frame)
    key = cv2.waitKey() & 0xFF

    if key == ord("q"):
        break

print("[INFO] saaf safiye")
csv.close()
cv2.destroyAllWindows()
vs.stop()
