# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster
WORKDIR /app
COPY . . 
RUN pip3 install -r requirements.txt
EXPOSE 5000
CMD [ "python3","main.py","--host=0.0.0.0", "--port=5000"]