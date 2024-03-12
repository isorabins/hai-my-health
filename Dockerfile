FROM python:3.10-slim-bullseye


WORKDIR /app
COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt
RUN apt update && apt install -y ffmpeg

COPY ./app /app

ENTRYPOINT [ "python3", "bot/gpt_telegram_bot.py" ]