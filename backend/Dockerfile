FROM python:3.12-slim
LABEL authors="kalyuzhin"

WORKDIR /backend/
COPY ./backend/requirements.txt /backend/
RUN pip3.12 install -Ur /backend/requirements.txt
RUN apt-get update && apt-get install flac -y
COPY ./backend /backend/