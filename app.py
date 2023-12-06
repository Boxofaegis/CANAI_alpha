from urllib import response
import openai
import speech_recognition as sr
import time, os,sys
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from selenium import webdriver

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from CAN_speaker import *
from CAN_terminal_chat import *

openai.api_key = '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'
driver = webdriver.Chrome()
app = Flask(__name__, template_folder="templates")

CORS(app, resources={r"/*": {"origins": "*"}})
# Replace this function with your actual get_response function

@app.route('/static/css/TeamCan.css')
def get_css():
    return app.send_static_file('css/TeamCan.css')
@app.route('/')
def index():
    return render_template('TeamCan.html')
@app.route('/chat')
def Chating():
    return render_template('Chating.html')
@app.route('/home')
def TeamCan():
    return render_template('TeamCan.html')

@app.route('/get_response', methods=['POST'])
def get_bot_response():
    user_input = request.form['user_input']
    if user_input.lower() == '종료':
        return "채팅을 종료합니다."
    else:
        gpt_response = get_response(user_input)
        return gpt_response
    
@app.route('/process_voice', methods=['POST'])
def process_voice():
    r=sr.Recognizer()
    m=sr.Microphone()
    CAN_speak('무엇을 도와드릴까요?','ko')
    start_CAN=r.listen_in_background(m,CAN_listen)
    CAN_answer(start_CAN,language='ko')
    return jsonify({response:start_CAN})
    
        

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)