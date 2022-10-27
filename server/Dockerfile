FROM python:3.8-alpine
WORKDIR /app
COPY . /app
COPY ./requirements.txt /app/requirements.txt
RUN pip3 install pika && \
    pip3 install -r requirements.txt
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]