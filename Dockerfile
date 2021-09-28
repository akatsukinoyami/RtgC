FROM python:3.9-slim-buster
WORKDIR /app/
COPY ./pyrogram.txt .
RUN ["pip3", "install", "-r", "pyrogram.txt"]
COPY . .