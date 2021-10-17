FROM python:3.9-alpine

WORKDIR /usr/src/tts

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

CMD FLASK_APP=tts flask run --host=0.0.0.0

COPY *.py ./
