import cv2
import matplotlib.pyplot as plt
import numpy as np

corner_track_params = dict( maxCorners=1, qualityLevel = 0.3, minDistance=7, blockSize=7)
lk_params = dict( winSize=(200,200), maxLevel=2, criteria= (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10,0.03 ) )

cap = cv2.VideoCapture(0)

ret, prev_frame = cap.read()
prev_gray = cv2.cvtColor( prev_frame, cv2.COLOR_BGR2GRAY)

# Pts to Track
prevpts = cv2.goodFeaturesToTrack( prev_gray, mask=None, **corner_track_params)
mask = np.zeros_like(prev_frame) # This will hold the motion history lines

while True:
    ret, frame = cap.read() # Capture the next live frame.
    frame_gray = cv2.cvtColor( frame, cv2.COLOR_BGR2GRAY)

    nextpts, status, err = cv2.calcOpticalFlowPyrLK( prev_gray, frame_gray, prevpts, None,**lk_params)

    # Filters out points that could not be tracked reliably.
    good_new = nextpts[status==1]
    good_prev = prevpts[status==1]

    # Draw the motion
    for i, (new,prev) in enumerate( zip(good_new,good_prev) ):
        x_new, y_new = new.ravel()
        x_new, y_new = int(x_new), int(y_new)
        x_prev, y_prev = prev.ravel()
        x_prev, y_prev = int(x_prev), int(y_prev)

        mask = cv2.line( mask, (x_new,y_new), (x_prev,y_prev), [0,255,0], 3) # Line on mask → motion path (history)
        frame = cv2.circle( frame, (x_new,y_new), 8, [0,0,255], -1) # Circle on frame → current position

    img = cv2.add(frame, mask) # Adds mask (history) to live video feed → you see both trajectory and live points.
    cv2.imshow("Tracking", img)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break


    prev_gray = frame_gray.copy()
    prevpts= good_new.reshape(-1,1,2)

cap.release()
cv2.destroyAllWindows