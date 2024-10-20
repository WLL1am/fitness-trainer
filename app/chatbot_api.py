from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chatbot', methods=['GET', 'POST'])
def chatbot():
    if request.method == 'POST':
        user_msg = request.json.get('message')
        headers = {'Content-Type': 'application/json'}
        rasa_url = "http://localhost:5005/webhooks/rest/webhook"
        
        try:
            response = requests.post(rasa_url, json={"sender": "user", "message": user_msg}, headers=headers)
            response.raise_for_status()
            return jsonify(response.json())
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return jsonify({"error": "HTTP error occurred"}), 500
        except requests.exceptions.JSONDecodeError:
            print("Failed to decode JSON response")
            return jsonify({"error": "Invalid JSON response"}), 500
        except Exception as err:
            print(f"Other error occurred: {err}")
            return jsonify({"error": "An unexpected error occurred"}), 500
        
    return "Chatbot endpoint. Use POST to send a message."

if __name__ == '__main__':
    app.run(port=5000, debug=True)