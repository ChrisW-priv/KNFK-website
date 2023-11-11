FROM python:3.11-alpine

COPY ./requirements.txt ./
RUN pip install -r ./requirements.txt

COPY . /app/
WORKDIR /app

COPY ./entrypoint.sh /

CMD ["./entrypoint.sh"]

