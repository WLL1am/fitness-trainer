# Fitness Trainer Application

## Overview
This project is a Fitness Trainer web application that integrates pose detection technology with a chatbot API for real-time user interactions. It captures live video, performs pose corrections, and allows users to interact with a chatbot to receive feedback.

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