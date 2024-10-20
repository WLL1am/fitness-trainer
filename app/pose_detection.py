import cv2
import mediapipe as mp
import numpy as np
import torch 
import requests
from app.models.pose_correction_model import PoseCorrectionModel


def calculate_angle(x, y, z):
    x = np.array(x)
    y = np.array(y)
    z = np.array(z)
    
    angleRadians = np.arctan2(z[1] - y[1], z[0] - y[0]) - np.arctan2(x[1] - y[1], x[0] - y[0])
    angleDegrees = np.abs(angleRadians * 180.0 / np.pi)
    
    if angleDegrees > 180.0:
        angleDegrees = 360 - angleDegrees
        
    return angleDegrees

def send_to_chatbot(message):
    response = requests.post('http://localhost:5000/chatbot', json={'message': message})
    return response.json()



# init MediaPip pose model
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_draw = mp.solutions.drawing_utils
model = PoseCorrectionModel()
model.eval()

dummy_input = torch.randn(1, 34)
with torch.no_grad():
    output = model(dummy_input)
    print(output)

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
        
        left_hip = (processed.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP].x,
                    processed.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP].y)
        left_knee = (processed.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP].x,
                    processed.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_KNEE].y)
        left_ankle = (processed.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ANKLE].x,
                    processed.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ANKLE].y)
        
        knee_angle = calculate_angle(left_hip, left_knee, left_ankle)
        
        if knee_angle < 90:
            feedback = "Squat too deep!"
            send_to_chatbot("What do you think of my squat form?")
            cv2.putText(frame, "Squat too low!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        elif knee_angle > 110:
            cv2.putText(frame, "Squat not deep enough!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        else: 
            cv2.putText(frame, "Nice squat!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)            
    
    cv2.imshow('Pose Estimation', frame)
    
    # quit w/ 'q'
    if cv2.waitKey(1) &0xFF == ord('q'):
        break
    
cam.release()
cv2.destroyAllWindows()