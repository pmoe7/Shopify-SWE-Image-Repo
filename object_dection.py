# app.py
# Mohammed Perves
# April 30, 2021

import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
import sys

def detect(img):
    """
        Parameters
        ----------
        img : str
            path to image file
        
        Returns
        -------
        list
            a list of strings used that are the header columns
    """

    # ensure we have a path to a file
    assert img != None, "Please provide a path to an image file"
    assert type(img) == str, "Please provide a valid path to an image file in string format like so 'path/to/image.png'"
    
    try:
        # read image from the path given
        im = cv2.imread(img)
        # use cvlib to detect objects in the image and only return labels that have a confidence of 70% or more
        _, labels, _ = cv.detect_common_objects(im, confidence=0.7, nms_thresh=0.3, model='yolov3', enable_gpu=False)
        return labels
        #output_image = draw_bbox(im, bbox, label, conf)

    except OSError as err:
        print("OS error: {0}".format(err))
    except ValueError as err:
        print("Value error: {0}".format(err))
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

    return []

#print(detect('static/uploads/me1.png'))\