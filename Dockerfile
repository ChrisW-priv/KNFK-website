FROM python:3.11

WORKDIR /app

COPY ./requirements.txt ./

RUN pip install -r ./requirements.txt

COPY . .

RUN python3 manage.py collectstatic

ENV PORT=8000

EXPOSE 8000

CMD ["./entrypoint.sh"]

