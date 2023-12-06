import time
from tracemalloc import start
from typing import cast
import webbrowser
import click
from numpy import can_cast
from openai.openai_object import OpenAIObject
import openai

from selenium import webdriver
import speech_recognition as sr
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from CAN_speaker import *

import requests
openai.api_key = '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'
driver = webdriver.Chrome()

r=sr.Recognizer()
m=sr.Microphone()

start_listening=r.listen_in_background(m,CAN_listen)


def CAN_command_ko(command,language_a):#추가적인 기능 부여
 

    if any('검색' in word for word in command.split()):
            search_query = command.replace('검색', '').strip()
            search_url = f"https://www.google.com/search?q={search_query}"
            webbrowser.open_new(search_url)
            ta=f'요청하신 검색 사항을 찾기위해 구글을 실행합니다.'
            
            print(ta)
            CAN_answer(ta,language_a)
            CAN_save_gpt(command)

    if any(word in command for word in ['멈춰', '그만', '정지']):
            start_listening(wait_for_stop=False)
            #stop_listening(wait_for_stop=False)
            ta='캔 음성 정지'
            print(ta)
            
            CAN_answer(ta,language_a)
            CAN_save_gpt(command)
    elif any(['터미널','채팅'] in word for word in command.split()):
            if any(word in command for word in ['시작','작동','사용']):
                import gpt3_terminal_chat
                gpt3_terminal_chat.start_terminal_chat()
                ta='터미널 채팅 시작'
                
                CAN_answer(ta,language_a)
                CAN_save_gpt(command)
    elif any(['대화','음성'] in word for word in command.split()):    
            if any(word in command for word in ['시작','작동','사용']):
                start_listening(wait_for_stop=True)   
                ta='캔 대화 시작'
            
                CAN_answer(ta,language_a)
                CAN_save_gpt(command)
    elif start_listening:
    # 다른 조  건 추가 가능
      
        in_text = openai.ChatCompletion.create(model="gpt-3.5-turbo",
            messages=[{"role":"user","content":command}],max_tokens=50)
        in_text = cast(OpenAIObject, in_text)
#        if in_text.status_code == 200:
        answer_text = in_text['choices'][0]['message']['content']

       
        CAN_speak(answer_text, language_a)
        CAN_save_gpt(answer_text)
        
            
    else:
        answer_text = "의미를 모르겠습니다."
        CAN_speak(answer_text, lang=language_a)
        CAN_save_gpt(answer_text)

 

           # if language=='en':
        #     if ['stop listen',''] == input_text:
        #         is_listening = False  # Update the listening flag
        #         stop_listening(wait_for_stop=False)
        #     elif 'CAN' == input_text:
        #         is_listening = True  # Set listening to True on 'CAN' command
        #     elif 'start terminal'==input_text:
        #         gpt3_terminal_chat.start_terminal_chat()
        #elif is_listening:
            
          #  response = requests.post(url, json=data, headers=headers)
         #   if response.status_code == 200:
           #     answer_text = response.json()['choices'][0]['text'].strip()
                
            #    speak(answer_text, lang=detected_language)
            #else:
             #   answer_text = "Sir. 의미를 모르겠습니다."
              #  speak(answer_text, lang=detected_language)
              
              
# #번역
# def translate(text, target_language='en'):
#     endpoint = f"https://translation.googleapis.com/language/translate/v2?key={GOOGLE_TRANSLATE_API_KEY}"
#     data = {
#         'q': text,
#         'target': target_language
#     }
#     response = requests.post(endpoint, data=data)
#     if response.status_code == 200:
#         translation = response.json()['data']['translations'][0]['translatedText']
#         return translation
#     else:
#         return "Translation failed."
