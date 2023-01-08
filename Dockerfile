
FROM python:3

WORKDIR /app

COPY requirements.txt ./

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000

cmd ["gunicorn", "-w", "1", "-b", "0.0.0.0:8000", "app:app"]