import cv2 as cv
from imutils.video.pivideostream import PiVideoStream
import imutils
import time
import numpy as np


class VideoCamera(object):
    def __init__(self, flip = False, file_type  = ".jpg"):
        
        self.video_stream = PiVideoStream()
        self.flip = flip
        self.file_type = file_type 

    def delete(self):
        self.vs.stop()
        time.sleep(2)
        
    def start(self):
        self.vs = self.video_stream.start()
        time.sleep(2)

        

    def flip_if_needed(self, frame):
        if self.flip:
            return np.flip(frame, 0)
        return frame

    def get_frame(self):
        frame = self.flip_if_needed(self.vs.read())
        ret, jpeg = cv.imencode(self.file_type, frame)
        self.previous_frame = jpeg
        return jpeg.tobytes()
