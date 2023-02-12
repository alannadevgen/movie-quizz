FROM python:latest

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY setup.py setup.py

RUN pip install -e .

COPY . .

ENTRYPOINT ["python", "webservice/app.py"]