FROM python:3.11-alpine

ENV PATH=/root/.local/bin:$PATH

COPY requirements.txt .
RUN pip install --user -r requirements.txt

WORKDIR /
COPY ./proxy ./proxy

EXPOSE 5000
CMD ["python3", "-m", "proxy"]
