import cv2 as cv
from theme.theme import *

def printStats(counter, minAngle, maxAngle):
    print('='*25)
    print('|- Number of REPS:', counter)
    print('|- Lowest angle:', round(minAngle, 2))
    print('|- Highest angle:', round(maxAngle, 2))
    print('='*25)

def renderStatusBox(image, counter, depthAngle, tilt, stance, stage):
    # Create a transparent background rectangle for better readability
    cv.rectangle(image, (0, 0), (280, 165), statusBox, -1)

    # Set font properties
    font = cv.FONT_HERSHEY_SIMPLEX
    fontScale = 0.7
    fontThickness = 2

    # Display "REPS" label and value
    cv.putText(image, 'REPS:', (15, 30), font, fontScale, statusLabel, fontThickness, cv.LINE_AA)
    cv.putText(image, str(counter).lower(), (120, 30), font, fontScale, repColor, fontThickness, cv.LINE_AA)

    # Display "ANGLE" label and value
    cv.putText(image, 'ANGLE:', (15, 60), font, fontScale, statusLabel, fontThickness, cv.LINE_AA)
    cv.putText(image, f'{int(depthAngle)} deg', (120, 60), font, fontScale, statusValue, fontThickness, cv.LINE_AA)

    # Display "STAGE" label and value
    cv.putText(image, 'STAGE:', (15, 90), font, fontScale, statusLabel, fontThickness, cv.LINE_AA)
    cv.putText(image, str(stage).lower(), (120, 90), font, fontScale,statusValue, fontThickness, cv.LINE_AA)

    # Display "TILT" label and value
    cv.putText(image, 'TILT:', (15, 120), font, fontScale, statusLabel, fontThickness, cv.LINE_AA)
    cv.putText(image, str(tilt).lower(), (120, 120), font, fontScale, statusValue, fontThickness, cv.LINE_AA)

    # Display "STANCE" label and value
    cv.putText(image, 'STANCE:', (15, 150), font, fontScale, statusLabel, fontThickness, cv.LINE_AA)
    cv.putText(image, str(stance).lower(), (120, 150), font, fontScale, statusValue, fontThickness, cv.LINE_AA)