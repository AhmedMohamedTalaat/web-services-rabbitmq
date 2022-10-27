import pika


if __name__ == '__main__':
    print("connecting to server!")
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host="rabbitmq"))
        channel = connection.channel()
    except pika.exceptions.AMQPConnectionError as ex:
        print("Failed to connect to RabbitMQ service. Message wont be sent.")
channel.queue_declare(queue='task_queue', durable=True)

print(' Waiting for messages...')

def callback(ch, method, properties, body):
    print(f"Received ===> {body.decode()}")
    print("Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue',
                        on_message_callback=callback)
channel.start_consuming()
