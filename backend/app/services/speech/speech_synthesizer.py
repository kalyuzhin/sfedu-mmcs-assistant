import io
import pyttsx3
import requests

from backend.app.services.api import settings
from gtts import gTTS


class SpeechSynthesizer:
    def __init__(self):
        pass

    @staticmethod
    def synthesize_speech_gtts(text: str) -> bytes:
        buffer = io.BytesIO()
        speech = gTTS(text=text, lang='ru', slow=False)
        speech.write_to_fp(buffer)

        return buffer.getvalue()

    @staticmethod
    def synthesize_speech_salute(text: str) -> bytes:
        headers = {
            'Content-Type': 'application/text',
            'Accept': 'audio/x-wav',
            'Authorization': f'Bearer {settings.SBER_TOKEN}'
        }
        payload = text
        resp = requests.post(settings.SYNTHESIZE_SBER_ENDPOINT, headers=headers, data=payload, verify=settings.CERTS)
        if resp.status_code != 200:
            print("Status code not successful")

            return b''

        return resp.content

    @staticmethod
    def synthesize_speech_pyttsx(text: str) -> None:
        engine = pyttsx3.init()
        engine.setProperty('volume', 1.0)
        engine.setProperty("rate", 200)
        engine.say(text)
        engine.runAndWait()
