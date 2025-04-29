import os
import asyncio
import pygame
import requests
import speech_recognition as sr

from dotenv import load_dotenv

load_dotenv()

SBER_TOKEN = os.getenv("SBER_TOKEN")
CERTS = os.getenv("CERTS")


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
        "RqUID": "aa7054a5-6419-40e5-b271-7ff0b83b9a12",
        "Authorization": f"Basic {SBER_TOKEN}"
    }

    return requests.post(url, headers=headers, data=payload, verify=CERTS).text


def write_audio() -> bytes:
    microphone = sr.Microphone()
    recognizer = sr.Recognizer()
    with microphone:
        recognizer.adjust_for_ambient_noise(microphone, duration=1)
        try:
            print("Слушаю...")
            audio = recognizer.listen(microphone)
        except sr.WaitTimeoutError as e:
            raise e

    return audio.get_wav_data()


def play_audio(filename: str) -> None:
    pygame.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

# print(get_sber_token())
