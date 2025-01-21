import speech_recognition as sr


def recognize_speech(recognizer: sr.Recognizer, microphone: sr.Microphone) -> str:
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


def main() -> None:
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    print(recognize_speech(recognizer, microphone))


if __name__ == "__main__":
    main()
