FROM python:3.7.9-slim

WORKDIR /resume
COPY . /resume

RUN pip install -r requirements.txt

EXPOSE 88
CMD ["pelican", "--listen"]