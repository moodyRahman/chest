
FROM python:3

COPY requirements.txt requirements.txt
COPY . .
RUN pip3 install -r requirements.txt
ENV chest_debug="true"
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]