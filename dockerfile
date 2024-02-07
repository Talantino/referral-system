FROM python:3.9
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /backend

RUN pip install --upgrade pip
COPY related.txt ./
RUN pip install -r related.txt
COPY run.sh /run.sh
RUN chmod +x /run.sh

COPY . /backend/
