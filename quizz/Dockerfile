FROM python:latest

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

WORKDIR /webservice

ENTRYPOINT ["flask", "run", "--host=0.0.0.0", "--port=80"]
