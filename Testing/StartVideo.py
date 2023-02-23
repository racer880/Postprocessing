import numpy as np
import cv2


class StartVideo():
    def __init__(self, path, video_1, video_2, video_3, video_4):
        #input
        names = [str(path) + "\\" + str(video_1), str(path) + "\\" + str(video_2), str(path)
                 + "\\" + str(video_3), str(path) + "\\" + str(video_4)]
        window_titles = [video_1, video_2, video_3, video_4]
        if video_4 is None:
            names.pop()
            window_titles.pop()
        if video_3 is None:
            names.pop()
            window_titles.pop()
        if video_2 is None:
            names.pop()
            window_titles.pop()
        if video_1 is None:
            names.pop()
            window_titles.pop()


        cap = [cv2.VideoCapture(i) for i in names]

        frames = [None] * len(names);
        gray = [None] * len(names);
        ret = [None] * len(names);

        while True:

            for i, c in enumerate(cap):
                if c is not None:
                    ret[i], frames[i] = c.read();

            for i, f in enumerate(frames):
                if ret[i] is True:
                    gray[i] = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
                    cv2.imshow(window_titles[i], gray[i]);

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        for c in cap:
            if c is not None:
                c.release();

        cv2.destroyAllWindows()
