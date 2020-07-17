FROM python:3.6-alpine

VOLUME /app
COPY ./proxy/ /app/proxy
COPY requirements.txt /app

WORKDIR /app
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python3", "-m", "proxy"]

