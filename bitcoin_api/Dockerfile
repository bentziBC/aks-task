FROM python:3.10-slim

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 80

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:80", "api:app"]

