FROM python:3.8-slim

RUN apt-get update
RUN pip install --no-cache-dir --upgrade pip

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 9000

ENV FLASK_ENV=development
ENV FLASK_APP=main.py
ENV FLASK_RUN_PORT=9000
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["flask", "run"]
