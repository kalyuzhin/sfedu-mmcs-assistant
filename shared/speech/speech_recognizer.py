import io
import wave
import speech_recognition as sr


class SpeechRecognizer:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def recognize_speech_bytes(self, audio_bytes: bytes) -> str:
        with wave.open(io.BytesIO(audio_bytes), 'rb') as wf:
            sample_rate = wf.getframerate()
            sample_width = wf.getsampwidth()
            frame_data = wf.readframes(wf.getnframes())
        audio_data = sr.AudioData(frame_data, sample_rate, sample_width)
        try:
            text = self.recognizer.recognize_google(audio_data, language="ru")
        except sr.UnknownValueError:
            raise RuntimeError("Не удалось распознать речь из предоставленных байтов")
        except sr.RequestError as e:
            raise RuntimeError(f"Ошибка сервиса распознавания: {e}")

        return text
