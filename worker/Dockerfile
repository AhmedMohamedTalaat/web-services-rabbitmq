FROM python:3.8-alpine
RUN pip3 install pika
WORKDIR /app
COPY . /app
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]