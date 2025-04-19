FROM python:3.12-slim
LABEL authors="kalyuzhin"

WORKDIR /app/
COPY ./requirements.txt /app
RUN apt-get update && apt-get install -y ffmpeg gcc libportaudio2 portaudio19-dev
RUN pip3.12 install -U pip && pip3.12 install -Ur requirements.txt
COPY . /app
EXPOSE 8080

CMD ["python3","main.py"]