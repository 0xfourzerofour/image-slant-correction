from correct import four_point_transform
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image file")
# ap.add_argument("-c", "--coords",
	# help = "comma seperated list of source points")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

boxes = []

def on_mouse(event, x, y, flags, params):

    if event == cv2.EVENT_LBUTTONUP and len(boxes) != 4:
        ebox = [x, y]
        boxes.append(ebox)
        
while(1):
    k = cv2.waitKey(33)

    if k==27:    # Esc key to stop
        cv2.destroyAllWindows()
        break

    img = cv2.imread(args["image"])
    img = cv2.blur(img, (3,3))

    if(len(boxes) < 4):

        cv2.namedWindow('real image')
        cv2.setMouseCallback('real image', on_mouse, 0)
        cv2.imshow('real image', img)
        cv2.waitKey(0)

    if(len(boxes) >= 4):

        coords = np.array(boxes)

        pts = np.array(boxes, np.int32)

        pts = pts.reshape((-1, 1, 2))

        isClosed = True

        line_thickness = 3
        cv2.polylines(img, [pts], isClosed, (0, 255, 0), line_thickness)

        cv2.imshow('image', img)
        cv2.waitKey(0)

        warped = four_point_transform(image, coords )
        cv2.imshow("Warped", warped)
        cv2.waitKey(0)


        cv2.destroyAllWindows()
        break



  




# pts = np.array(eval(args["coords"]), dtype = "float32")

# warped = four_point_transform(image, pts)

# cv2.imshow("Original", image)
# cv2.imshow("Warped", warped)
