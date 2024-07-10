from flask import Flask, request, jsonify, render_template_string
from werkzeug.utils import secure_filename
import os
from process import Process
import time
import json
# import firebase_admin
# import sys
# sys.stdout.default_encoding = 'utf-8'
process = Process()
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

@app.route('/')
def index():
    return render_template_string()

def upload_text():
    if 'text' not in request.form:
        return 'No text part'
    text = request.form['text']
    if text == '':
        return 'No text provided'
    
    st_time = time.time()

    ai_response = process.chatBot(text)

    end_time = time.time()
    
    
    print("time: ",end_time - st_time)

    return jsonify({'status': 'file uploaded and archived',
                    'result':{"user_prompt":text, "ai_response":ai_response}})

if __name__ == '__main__':
    app.run(debug=True)
