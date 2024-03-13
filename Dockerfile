FROM python:3.10-slim-bullseye


WORKDIR /app
COPY requirements.txt requirements.txt
# Add a step to invalidate the cache starting from here
ADD "https://www.random.org/cgi-bin/randbyte?nbytes=10&format=h" skipcache

# Then copy your requirements.txt and install your Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --force-reinstall -r requirements.txt

#RUN pip install --no-cache-dir -r requirements.txt
#RUN pip install -r requirements.txt
RUN apt update && apt install -y ffmpeg



COPY ./app /app

ENTRYPOINT [ "python3", "bot/gpt_telegram_bot.py" ]