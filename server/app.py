from ast import ExceptHandler
from flask import Flask
import pika

app = Flask(__name__)


@app.route('/create-message/<msg>')
def add(msg):
    try:
        conn = pika.BlockingConnection(
            pika.ConnectionParameters(host='rabbitmq'))
        channel = conn.channel()
        r=channel.queue_declare(queue='task_queue',
                              durable=True)
        channel.basic_publish(exchange='',
                              routing_key='task_queue',
                              body=msg,
                              properties=pika.BasicProperties(delivery_mode=2))
        conn.close()
    except pika.exceptions.AMQPConnectionError as ex:
        print("Failed to connect to RabbitMQ service.")
        return ex.__str__()
    return f"the command :{msg}"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
