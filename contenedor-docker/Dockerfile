FROM python:3.11

WORKDIR /app

COPY main.py .
COPY config.ini .
COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt

ENV DISPLAY host.docker.internal:0

CMD ["python", "main.py"]