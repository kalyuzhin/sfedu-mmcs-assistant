import os
import ssl
import wave
import speech_recognition as sr
import pyttsx3
from gtts import gTTS

recognizer = sr.Recognizer()
microphone = sr.Microphone()


def recognize_speech_sr() -> str:
    with microphone:
        data = ""
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


def recognize_speech_whisper() -> str:
    with microphone:
        audio = recognizer.listen(microphone)
    save_wave("whisper.wav", audio)
    model = whisper.load_model("tiny")
    result = model.transcribe("whisper.wav")
    return result["text"]


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
