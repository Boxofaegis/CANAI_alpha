import openai
import json
import speech_recognition as sr
import time, os
from gtts import gTTS
from playsound import playsound



openai.api_key = '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'

# GOOGLE_TRANSLATE_API_KEY = 'YOUR_GOOGLE_TRANSLATE_API_KEY'
r=sr.Recognizer()

#음성 인식(듣기,STT)
language_models = {
    'ko': sr.Microphone(device_index=0),  # Korean language model
    'en': sr.Microphone(device_index=1),  # English language model
    
}
def CAN_listen(recognizer, audio):
    lang='ko'
    try:
        
        if lang in language_models.items():
            try:
                detected_language = lang
                text = recognizer.recognize_google(audio, language=detected_language)
                print(f'[나 - {detected_language}]: {text}')
                CAN_answer(text, detected_language)
                return  # 첫 번째 인식된 언어로 인식하고 종료    
            except sr.UnknownValueError:
                
                CAN_speak('언어 인식 실패', lang)
    except sr.RequestError as e:
        CAN_speak('요청 실패:{0}'.format(e),lang)    

#대답
def CAN_answer(input_text, language):
    global is_listening
    ko_in=input_text
    lang_in=language
    
    try:#임시
        if language=='ko':    
            from CAN_modul.CAN_somthing_ko import CAN_command_ko
            answer_text=CAN_command_ko(ko_in,lang_in)#한국어라면 open_somthing_ko로 가서 판단(ko,en 등의 각 나라별로 제작할것)
            CAN_speak(answer_text,language)
            return answer_text
        elif language=='en':
            pass
        elif language=='ja':
            pass
 
    except Exception as e:
        print(f"Error accessing GPT-3 API: {e}")
        answer_text = "rquest에서 오류가 발생했습니다."
        CAN_speak(answer_text, language)
        return answer_text
    

# GPT로부터 받은 예시 응답 (임의의 응답)
def CAN_save_gpt(answer_text):
    gpt_response = answer_text

        # 기존 데이터 파일이 있는 경우 읽어오고, 없으면 빈 리스트 생성
    try:
        with open('gpt_responses.json', 'r', encoding='utf-8') as file:
                responses = json.load(file)
    except FileNotFoundError:
            responses = []

        # 새 응답 추가
    responses.append({'response': gpt_response})

        # 응답을 JSON 파일에 저장
    with open('gpt_responses.json', 'w', encoding='utf-8') as file:
        json.dump(responses, file, ensure_ascii=False, indent=4)
    
#소리내어 읽기(TTS)
def CAN_speak(text, lang):
    print(f'[CAN - {lang}]: {text}')
    file_name='voice.mp3'
    tts=gTTS(text=text, lang=lang)
    tts.save(file_name)
    playsound(file_name)
    if os.path.exists(file_name):
        os.remove(file_name)

#m=sr.Microphone()
#CAN_speak('무엇을 도와드릴까요?','ko')
#r.listen_in_background(m,CAN_listen)#계속 듣기(listen 계속 호출)

#while True:
 #   time.sleep(0.1)
    
    
