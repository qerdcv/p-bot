FROM python:3.9-slim
WORKDIR bot
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY pidorbot/ .
