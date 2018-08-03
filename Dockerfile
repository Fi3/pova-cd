FROM python:3.7-alpine3.8
ADD . /code

WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python", "./src/app.py"]
