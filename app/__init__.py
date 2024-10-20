from flask import Flask, render_template
import cv2
from app.pose_detection import start_pose_detection