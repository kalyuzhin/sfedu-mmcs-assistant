import os
import wave
import time
import pyttsx3
import pygame
import requests
from gtts import gTTS
import speech_recognition as sr

recognizer = sr.Recognizer()
microphone = sr.Microphone()


def recognize_speech_sr() -> str:
    with microphone:
        data: str
        recognizer.adjust_for_ambient_noise(microphone, duration=2)
        try:
            print("Слушаю...")
            audio = recognizer.listen(microphone)
        except sr.WaitTimeoutError as e:
            print(f"Ошибка:\n{e}")
            exit(-1)
        try:
            data = recognizer.recognize_google(audio, language="ru")
        except sr.UnknownValueError:
            print("Не получилось обработать аудио")
            exit(-1)
    return data


def save_wave(filename: str, audio: sr.AudioData) -> None:
    with wave.open("audio.wav", "wb") as f:
        f.setnchannels(1)
        f.setsampwidth(audio.sample_width)
        f.setframerate(audio.sample_rate)
        f.writeframes(audio.get_raw_data())


def synthesize_speech_pyttsx(text: str) -> None:
    engine = pyttsx3.init()
    engine.setProperty('volume', 1.0)
    engine.setProperty("rate", 200)
    engine.say(text)
    engine.runAndWait()


def synthesize_speech_gtts(text: str) -> None:
    speech = gTTS(text=text, lang='ru', slow=False)
    speech.save("output.mp3")
    os.system("open output.mp3")


def synthesize_speech_salute(text: str) -> None:
    URL = f"https://smartspeech.sber.ru/rest/v1/text:synthesize"
    headers = {
        'Content-Type': 'application/text',
        'Accept': 'audio/x-wav',
        'Authorization': f'Bearer {TOKEN}'
    }
    payload = text
    resp = requests.post(URL, headers=headers, data=payload,
                         verify='/Users/kalyuzhin/Downloads/russiantrustedca/russiantrustedca.pem')
    if resp.status_code != 200:
        print("Status code not successful")
        return
    with open("file.wav", "wb") as f:
        f.write(resp.content)

    play_audio("file.wav")


def play_audio(filename: str) -> None:
    pygame.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    pygame.event.wait()

# start = time.time()
# for i in range(100):
#     synthesize_speech_salute("Привет")
# end = time.time()
# play_audio("file.wav")
#
