FROM python:3.11-slim-buster

WORKDIR /app

COPY . .

RUN pip install -r src/requirements.txt

RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]

