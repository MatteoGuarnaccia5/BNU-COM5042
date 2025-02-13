FROM python:3.11

WORKDIR /app
COPY main.py ./app.py

EXPOSE 8080

CMD python app.py