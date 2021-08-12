FROM python:3.9

WORKDIR /api

COPY sources.list /etc/apt/
COPY requirements.txt .

RUN apt-get -q update && apt-get -qy install netcat
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "-u", "-m", "src.app"]