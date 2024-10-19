import cv2
import mediapipe as mp

# init MediaPip pose model
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_draw = mp.solutions.drawing_utils

# init webcam
cam = cv2.VideoCapture(0)

while cam.isOpened():
    ret, frame = cam.read()
    
    if not ret:
        break
    
    # convert frames to RGB for processing
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    processed = pose.process(rgb_frame)
    
    # landmarks and connections
    if processed.pose_landmarks:
        mp_draw.draw_landmarks(frame, processed.pose_landmarks, mp_pose.POSE_CONNECTIONS)
    
    cv2.imshow('Pose Estimation', frame)
    
    # quit w/ 'q'
    if cv2.waitKey(1) &0xFF == ord('q'):
        break
    
cam.release()
cv2.destroyAllWindows()