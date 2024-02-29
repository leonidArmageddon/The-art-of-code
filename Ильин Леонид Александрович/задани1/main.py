import speech_recognition as sr
import pyttsx3
import nltk
from nltk.chat.util import Chat, reflections
import webbrowser
import subprocess

engine = pyttsx3.init()

recognizer = sr.Recognizer()

pairs = [
    ['привет', ['привет', 'здравствуй']],
    ['как дела?', ['Хорошо, спасибо!']],
    ['открой калькулятор', ['открываю калькулятор', 'калькулятор открыт']],

]

chatbot = Chat(pairs, reflections)

def process_speech():
    with sr.Microphone() as source:
        print("Говорите что-нибудь:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language='ru-RU')
        print("Вы сказали:", text)
        return text
    except sr.WaitTimeoutError:
        print("Истекло время ожидания речи")
    except sr.UnknownValueError:
        print("Извините, не могу распознать речь")
    except sr.RequestError:
        print("Ошибка в сети; не удалось получить ответ от сервиса распознавания речи")
        return ""

def execute_command(command):
    if 'калькулятор' in command:
        subprocess.Popen('calc.exe', shell=True)
    elif 'браузер' in command:
        webbrowser.open('https://www.google.com')

def speak(text):
    engine.say(text)
    engine.runAndWait()

while True:
    query = process_speech()

    if 'пока' in query.lower():
        speak("До встречи!")
        break

    response = chatbot.respond(query)
    if response:
        speak(response)
    else:
        execute_command(query)
