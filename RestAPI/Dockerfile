FROM python:3.9-slim

COPY . /app

RUN pip install flask gunicorn

WORKDIR /app

EXPOSE 80

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:80", "restapi:app"]