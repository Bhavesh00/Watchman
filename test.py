import numpy as np
import cv2


def saveVideo():
    cap = cv2.VideoCapture(0) # Capture video from camera

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('output.mp4', fourcc, 24.0, (width, height))

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            out.write(frame)

            cv2.imshow('frame',frame)
            if (cv2.waitKey(1) & 0xFF) == ord('q'): # Hit `q` to exit
                break
        else:
            break

    out.release()
    cap.release()
    cv2.destroyAllWindows()

saveVideo()