#! /usr/bin/python
import cv2
import yolov5
import numpy as np
import pandas as pd
import sys
from Capture import Capture


class Detection():
    def __init__(self):
        self.video = Capture()
        self.dice = np.array([])
        # Load pretrained model
        self.model = yolov5.load('best.pt')
        # Set model parameters
        self.model.conf = 0.75 # NMS confidence threshold
        self.model.iou = 0.45 # NMS IoU threshold
        self.model.agnostic = False # NMS class-agnostic
        self.model.multi_label = False # NMS multiple labels per box
        self.model.max_det = 5 # maximum number of detections per image
        self.colors = { 1:(108, 188, 77),
                        2:(212, 224, 86),
                        3:(241, 40, 68),
                        4:(226, 143, 81),
                        5:(88, 71, 151),
                        6:(59, 123, 189)}

    # Returns image with detection captions
    def get_img(self):

        self.dice = np.array([])
        ret, img = self.video.get_frame()
        results = self.model(img)

        for obj in results.pred[0]:
            x1, y1, x2, y2, conf, cat = obj.detach().cpu().numpy()
            # Add 1 to category to get the die face value
            x1, y1, x2, y2, cat = int(x1), int(y1), int(x2), int(y2), int(cat + 1)
            self.dice = np.append(self.dice, cat)
            if cat in self.colors.keys():
                # Construct bounding box
                cv2.rectangle(img, (x1, y1), (x2, y2), self.colors[cat], 2)
                # Write face value and confidence on top of the bounding box
                cv2.putText(img, f"{cat}   {conf:.2f}", (x1, y1-12), cv2.FONT_HERSHEY_SIMPLEX, 0.6, self.colors[cat], 2, 2)

        return img

    def get_dice(self):
        return self.dice