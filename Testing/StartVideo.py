import numpy as np
import cv2

names = ['../Files/Test.mp4', '../Files/Test_2.mp4'];
window_titles = ['My Wakeboard Experience', 'Travel around the world']


cap = [cv2.VideoCapture(i) for i in names]

frames = [None] * len(names);
gray = [None] * len(names);
ret = [None] * len(names);

while True:

    for i,c in enumerate(cap):
        if c is not None:
            ret[i], frames[i] = c.read();


    for i,f in enumerate(frames):
        if ret[i] is True:
            gray[i] = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
            cv2.imshow(window_titles[i], gray[i]);

    if cv2.waitKey(10) & 0xFF == ord('q'):
       break


for c in cap:
    if c is not None:
        c.release();

cv2.destroyAllWindows()