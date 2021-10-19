# -*- coding: utf-8 -*-
#!/usr/bin/python3
"""
Created on 2021/5/24 13:46
@Author: Wang Cong
@Email : iwangcong@outlook.com
@Version : 0.1
@File : demo_trt.py
"""
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'
import cv2
import time
import ctypes
import tracker
import random
from detector_trt import Detector


def detect(video_path, engine_file_path):
    detector = Detector(engine_file_path)
    capture = cv2.VideoCapture(video_path)
    # capture = cv2.VideoCapture(0)
    fps = 0.0
    while True:
        ret, img = capture.read()
        if img is None:
            print('No image input!')
            break

        line_thickness = 3

        t1 = time.time()
        bboxes = detector.detect(img)

        if len(bboxes) > 0:
            # list_bboxs = tracker.update(bboxes, img)
            output_image_frame = tracker.draw_bboxes(img, bboxes, line_thickness=1, color = (0, 255, 0))
        else:
            output_image_frame = img

        fps = (fps + (1. / (time.time() - t1))) / 2
        cv2.putText(output_image_frame, 'FPS: {:.2f}'.format(fps), (10, 20), 0, line_thickness/5, [0, 255, 0], thickness=1, lineType=cv2.LINE_AA)
        cv2.putText(output_image_frame, 'Time: {:.3f}'.format(time.time() - t1), (10, 40), 0, line_thickness/5, [0, 255, 0], thickness=1, lineType=cv2.LINE_AA)

        # cv2.putText(image, '{}:{:.2f}'.format(cls_id, conf), (c1[0], c1[1] - 2), 0, line_thickness / 3, [225, 255, 255], thickness=2, lineType=cv2.LINE_AA)
        if ret == True:
            cv2.imshow('frame', output_image_frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    capture.release()
    cv2.destroyAllWindows()
    detector.destroy()


if __name__ == '__main__':

    # video_path = 'video/test_2_720.mp4'
    video_path = '/dev/video1'
    PLUGIN_LIBRARY = "/home/xavier-dv/Desktop/tensorrtx/yolov5/build/libmyplugins.so"
    ctypes.CDLL(PLUGIN_LIBRARY)
    engine_file_path = '/home/xavier-dv/Desktop/tensorrtx/yolov5/build/yolov5m.engine'
    detect(video_path, engine_file_path)
