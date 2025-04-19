import asyncio
import requests
import speech_recognition as sr
from shared.core.config import settings


async def process_tasks_by_batches(data: list, batch_size: int, func) -> list:
    result = []
    for i in range(0, len(data), batch_size):
        batch = data[i:i + batch_size]
        result.extend(await asyncio.gather(*(func(item) for item in batch)))
    return result


def get_sber_token() -> str:
    url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
    payload = {
        'scope': 'SALUTE_SPEECH_PERS'
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json",
        "RqUID": "0b845cf3-969c-4cc1-b852-11819f93709c",
        "Authorization": f"Basic {settings.SBER_TOKEN}"
    }

    return requests.post(url, headers=headers, data=payload).text


def write_audio(filename: str = "test.wav"):
    microphone = sr.Microphone()
    recognizer = sr.Recognizer()
    with microphone:
        recognizer.adjust_for_ambient_noise(microphone, duration=1)
        try:
            print("Слушаю...")
            audio = recognizer.listen(microphone)
        except sr.WaitTimeoutError as e:
            raise e
    with open(filename, 'wb') as f:
        f.write(audio.get_wav_data())
