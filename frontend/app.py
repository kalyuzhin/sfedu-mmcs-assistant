import os
import sys
import requests

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from shared.scripts import play_audio, write_audio

URL = "http://127.0.0.1:9000/api/v1/rag/process"
OUTPUT_NAME = "output.mp3"


def main() -> None:
    start = input("Нажмите, чтобы начать")
    _bytes = write_audio()
    files = {"audio": ("audio.wav", _bytes, "audio/wav")}
    response = requests.post(URL, files=files)
    if response.status_code != 200:
        return
    with open(OUTPUT_NAME, "wb") as f:
        f.write(response.content)
    play_audio(OUTPUT_NAME)


if __name__ == '__main__':
    main()
