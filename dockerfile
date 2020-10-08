FROM python:alpine

WORKDIR /app

COPY ./requirements.txt ./


RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python3","app.py"]
