FROM python:latest

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

# WORKDIR /webservice

ENTRYPOINT ["python", "webservice/app.py", "flask", "run", "--host=0.0.0.0", "--port=80"]
