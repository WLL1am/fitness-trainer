# Fitness Trainer Application


## Overview
This project is a Fitness Trainer web application that integrates pose detection technology with a chatbot API for real-time user interactions. It captures live video, performs pose corrections, and allows users to interact with a chatbot to receive feedback.

**Web UI:**\
<img width="600" alt="Screenshot 2024-10-20 at 1 17 50 PM" src="https://github.com/user-attachments/assets/997db8de-15f8-4c16-bf08-2dccf3e1b35c">

**Good squats:**\
<img width="600" alt="Screenshot 2024-10-20 at 1 43 15 PM" src="https://github.com/user-attachments/assets/ee11ae16-08d1-430f-b1f4-6823465187b3">\
<img width="600" alt="Screenshot 2024-10-20 at 1 42 00 PM" src="https://github.com/user-attachments/assets/c716041b-e2f3-43f6-8a27-d28e600bcd72">

**Squats too low:**\
<img width="600" alt="Screenshot 2024-10-20 at 1 44 37 PM" src="https://github.com/user-attachments/assets/169d84b3-7bb6-4e80-a653-22057d995c82">\
<img width="600" alt="Screenshot 2024-10-20 at 1 43 40 PM" src="https://github.com/user-attachments/assets/eec95578-fd4c-4ac0-be42-2c13cf33b816">

**Squats not low enough:**\
<img width="600" alt="Screenshot 2024-10-20 at 1 45 05 PM" src="https://github.com/user-attachments/assets/796f90fa-81fa-4672-a389-a0b8a6544303">\
<img width="600" alt="Screenshot 2024-10-20 at 1 43 59 PM" src="https://github.com/user-attachments/assets/dc688430-004d-4618-b992-0923a853d087">


## Features
- **Live video streaming:** Uses the device's camera to capture real-time video.
- **Pose detection and correction:** Detects user movements and provides feedback on their exercise poses.
- **Chatbot interaction:** Allows users to send messages to a chatbot and receive responses in real-time.

## Project Structure
- `index.html`: The main frontend of the application. It displays the live video feed and provides an input for interacting with the chatbot.
- `pose_correction_model.py`: This Python script implements the machine learning model used to detect and correct user poses based on the video feed.
- `chatbot_api.py`: This script handles the chatbot API that receives user inputs and sends responses.
- `pose_detection.py`: Script to detect poses from the video feed and provide feedback to the user.
- `__init__.py`: Initializes and configures necessary modules for the pose detection and chatbot interaction.

## Installation
1. Clone the repository.
2. Install the necessary Python packages by running:
   ```bash
   pip install -r requirements.txt
3. Run "python chatbot_api.py" and "rasa run --enable-api" to start the chatbot API and rasa server. 
4. Go to the localhost url.
