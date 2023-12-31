import openai
from typing import cast
from openai.openai_object import OpenAIObject
from CAN_weather import *
from CAN_modul.city_name import *

def get_response(query):
   
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": query}],
            max_tokens=50
        )
        response = cast(OpenAIObject, response)
        return response['choices'][0]['message']['content']
    
def start_terminal_chat():
    print("채팅을 시작합니다. '종료'를 입력하여 대화를 종료할 수 있습니다.")

    while True:
        user_input = input("사용자: ")

        if user_input.lower() == '종료':
            print("채팅을 종료합니다.")
            break

                # 사용자 입력을 GPT-3로 보내고 응답 받기
        gpt_response = get_response(user_input)
        print(f"CAN(gpt3):{gpt_response}")#<<이게 터미널에 나와요


        if __name__ == "__main__":
            start_terminal_chat()
