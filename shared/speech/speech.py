import speech_recognition as sr

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
