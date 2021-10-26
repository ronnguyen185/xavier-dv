import cv2
import os
import glob
from natsort import natsorted

FPS = 30
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

video_name = '1280_30_D455_IR_L.mp4'
# video_name = '1280_30_D455_RGB.mp4'


images = glob.glob('1280_800_30/1612_2020__11_44_59/D455_1/IR/Left/*.jpg') 
# images = glob.glob('1280_800_30/1612_2020__11_44_59/D455_1/Color/*.jpg')
images.sort()
images = natsorted(images)

# print(images)
frame = cv2.imread(images[0])
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, fourcc, FPS, (width,height))

for image in images:
    print(image)
    video.write(cv2.imread(image))

cv2.destroyAllWindows()
video.release() 