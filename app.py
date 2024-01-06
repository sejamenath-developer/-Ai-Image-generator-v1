
from flask import Flask, render_template, request, jsonify
import os
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    user_prompt = request.form['user_prompt']
    api_key = os.environ.get('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')  # Access your API key stored in environment variables

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }

    # Make a request to your AI service API endpoint
    response = requests.post("https://api-inference.huggingface.co/models/dataautogpt3/OpenDalle", headers=headers, json={'inputs': user_prompt})

    if response.ok:
        # Process the response or get image URLs
        # Replace 'image_urls' with your actual response attribute
        image_urls = response.json().get('image_urls', [])
        return jsonify({'image_urls': image_urls})
    else:
        return jsonify({'error': 'Failed to generate images'}), 500

if __name__ == '__main__':
    app.run(debug=True)
