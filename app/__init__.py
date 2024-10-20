from flask import Flask, render_template
import cv2
from pose_detection import start_pose_detection

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    
    