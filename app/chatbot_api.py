from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_msg = request.json.get('message')
    headers = {'Content-Type': 'application/json'}
    rasa_url = "http://localhost:5005/webhooks/rest/webhook"
    
    response = requests.post(rasa_url, json={"sender": "user", "message": user_msg}, headers=headers)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(port=5000)