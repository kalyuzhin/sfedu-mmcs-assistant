import speech_recognition as sr


class SpeechRecognizer:
    def __init__(self):
        self.microphone = sr.Microphone()
        self.recognizer = sr.Recognizer()

    def recognize_speech_sr(self) -> str:
        with self.microphone:
            data: str
            self.recognizer.adjust_for_ambient_noise(self.microphone, duration=2)
            try:
                print("Слушаю...")
                audio = self.recognizer.listen(self.microphone)
            except sr.WaitTimeoutError as e:
                print(f"Ошибка:\n{e}")
                exit(-1)
            try:
                data = self.recognizer.recognize_google(audio, language="ru")
            except sr.UnknownValueError:
                print("Не получилось обработать аудио")
                exit(-1)
        return data
