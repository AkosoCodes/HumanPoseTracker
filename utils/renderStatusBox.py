import cv2 as cv
from theme.theme import *

def renderStatusBox(image, counter, depthAngle, tilt, stage):
    # Draw a semi-transparent background rectangle for better readability
    cv.rectangle(image, (0, 0), (225, 145), statusBox, -1)

    # Display "REPS" label
    cv.putText(image, 'REPS:', (15, 25), cv.FONT_HERSHEY_SIMPLEX, 0.7, statusLabel, 2, cv.LINE_AA)

    # Display the counter value
    cv.putText(image, str(counter), (100, 25), cv.FONT_HERSHEY_SIMPLEX, 0.7, statusValue, 2, cv.LINE_AA)

    # Display "ANGLE" label
    cv.putText(image, 'ANGLE:', (15, 60), cv.FONT_HERSHEY_SIMPLEX, 0.7, statusLabel, 2, cv.LINE_AA)

    # Display the angle value
    cv.putText(image, str(int(depthAngle)), (100, 60), cv.FONT_HERSHEY_SIMPLEX, 0.7, statusValue, 2, cv.LINE_AA)

    # Display the "STAGE" label
    cv.putText(image, 'STAGE:', (15, 95), cv.FONT_HERSHEY_SIMPLEX, 0.7, statusLabel, 2, cv.LINE_AA)

    # Display the stage value
    cv.putText(image, str(stage), (100, 95), cv.FONT_HERSHEY_SIMPLEX, 0.7, statusValue, 2, cv.LINE_AA)

    # Display the "TILT" label
    cv.putText(image, 'TILT:', (15, 130), cv.FONT_HERSHEY_SIMPLEX, 0.7, statusLabel, 2, cv.LINE_AA)
    
    # Display the tilt value
    cv.putText(image, str(tilt), (100, 130), cv.FONT_HERSHEY_SIMPLEX, 0.7, statusValue, 2, cv.LINE_AA)