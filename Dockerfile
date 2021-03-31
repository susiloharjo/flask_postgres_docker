FROM python:3-alpine

LABEL maintainer="susiloharjo@gmail.com"

COPY app /app

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# CMD [ "python", "main.py" ]



# sources
# https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx/