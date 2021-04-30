import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox

def detect(img=None):
    im = cv2.imread(img)
    bbox, label, conf = cv.detect_common_objects(im)
    #output_image = draw_bbox(im, bbox, label, conf)
    objects = []
    for c in conf:
        if c > 0.7:
            objects.append(label[conf.index(c)])
    #print(objects)
    return objects
