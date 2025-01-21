import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
microphone = sr.Microphone()


def recognize_speech() -> str:
    with microphone:
        data = ""
        # recognizer.adjust_for_ambient_noise(microphone, duration=2)
        try:
            print("Слушаю...")
            audio = recognizer.listen(microphone, timeout=5)
        except sr.WaitTimeoutError as e:
            print(f"Ошибка:\n{e}")
        try:
            data = recognizer.recognize_google(audio, language="ru-RU")
        except sr.UnknownValueError:
            print("Не получилось обработать аудио")
    return data


def synthesize_speech(text: str):
    engine = pyttsx3.init()
    engine.setProperty('volume', 1.0)
    engine.setProperty("rate", 180)
    engine.say(text)
    engine.runAndWait()
