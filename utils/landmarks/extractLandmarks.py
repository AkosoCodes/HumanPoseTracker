def extractLandmarks(results, mp_pose):
    """
    Extracts the landmarks for depth, tilt, and stance from the pose detection results.

    Parameters:
    - results: Pose detection results from MediaPipe.
    - mp_pose: MediaPipe pose object.

    Returns:
    - depthLandmarks: List of landmarks for the left hip, knee, and heel.
    - tiltLandmarks: List of landmarks for the right and left shoulders.
    - stanceLandmarks: List of landmarks for the left and right heels.
    """
    landmarks = results.pose_landmarks.landmark

    # Depth
    leftHip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x, landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
    leftKnee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x, landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
    leftHeel = [landmarks[mp_pose.PoseLandmark.LEFT_HEEL.value].x, landmarks[mp_pose.PoseLandmark.LEFT_HEEL.value].y]

    # Stance
    rightHeel = [landmarks[mp_pose.PoseLandmark.RIGHT_HEEL.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_HEEL.value].y]

    # Tilt
    leftShoulder = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value]
    rightShoulder = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value]

    # Landmark lists
    depthLandmarks = [leftHip, leftKnee, leftHeel]
    tiltLandmarks = [rightShoulder.y, leftShoulder.y]
    stanceLandmarks = [leftHeel, rightHeel]

    # Return
    return depthLandmarks, tiltLandmarks, stanceLandmarks