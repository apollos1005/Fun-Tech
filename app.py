from flask import Flask, request, jsonify
import time

app = Flask(__name__)

@app.route('/')
def index():
    return "AI Video Generator API is running."

@app.route('/generate', methods=['POST'])
def generate_video():
    data = request.get_json()
    prompt = data.get('prompt')
    if not prompt:
        return jsonify({'error': 'Prompt is required'}), 400
    # Simulate video generation
    time.sleep(3)
    return jsonify({'message': f"Generated video for prompt: '{prompt}'", 'video_url': '/static/sample_video.mp4'})
