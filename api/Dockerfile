FROM python:3.9.6-buster

WORKDIR /api

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "-u", "-m", "src.app"]