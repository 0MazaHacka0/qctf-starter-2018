FROM python:3.5

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 80

ENTRYPOINT ["./docker-entry-point.sh"]
