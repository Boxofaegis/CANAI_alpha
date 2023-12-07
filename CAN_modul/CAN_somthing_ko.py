import time
from tracemalloc import start
from typing import cast
import webbrowser
import click
from numpy import can_cast
from openai.openai_object import OpenAIObject
import openai
import speech_recognition as sr
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from CAN_speaker import *
from CAN_weather import *
from CAN_modul.city_name import *
import requests
openai.api_key = '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'


r=sr.Recognizer()
m=sr.Microphone()

start_listening=r.listen_in_background(m,CAN_listen)


def CAN_command_ko(command,language_a):#추가적인 기능 부여
        cities = city_w_name()

        if any('검색' in word for word in command.split()):
            search_query = command.replace('검색', '').strip()
            search_url = f"https://www.google.com/search?q={search_query}"
            webbrowser.open_new(search_url)
            return f'요청하신 검색 사항을 찾기위해 구글을 실행합니다.'

        if any(word in command for word in ['멈춰', '그만', '정지']):
                start_listening(wait_for_stop=False)
                return '캔 음성 정지'
                
        elif any('터미널' in word for word in command.split()):
                if any(word in command for word in ['시작','작동','사용']):
                        import gpt3_terminal_chat
                        gpt3_terminal_chat.start_terminal_chat()
                        return '터미널 채팅 시작'
                        
        elif any('대화' in word for word in command.split()):    
                if any(word in command for word in ['시작','작동','사용']):
                        # start_listening(wait_for_stop=True)   
                        ta='캔 대화 시작'
                        in_text = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                        messages=[{"role":"user","content":command}],max_tokens=50)
                        in_text = cast(OpenAIObject, in_text)
                #        if in_text.status_code == 200:
                        return in_text['choices'][0]['message']['content']

                        
                        
        # elif any('날씨' in word for word in command.split()): 
        #         if any(word in command for word in cities):
        #             for key, value in cities.items():
        #                 if key in command:
        #                     ta = CAN_weather_sr(value)
        #                     CAN_answer(ta,language_a)
        #                     CAN_save_gpt(command)            
                
                
        else:

                in_text = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                messages=[{"role":"user","content":command}],max_tokens=200)
                in_text = cast(OpenAIObject, in_text)
                return in_text['choices'][0]['message']['content']
                
        