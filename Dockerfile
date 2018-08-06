FROM python:3.7-alpine3.8
ADD . /code

WORKDIR /code
RUN apk add --update alpine-sdk
RUN pip install -r requirements.txt
CMD ["python", "./src/app.py"]
