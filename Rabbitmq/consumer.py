import pika

# establish a connection to RabbitMQ
connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

# declare a queue
channel.queue_declare(queue='letterbox')

# receive messages

def on_message_received(ch, method, properties, body):
    print(f"received new message: {body}")


channel.basic_consume(queue='letterbox', auto_ack=True,
    on_message_callback=on_message_received)

print("Starting Consuming")

channel.start_consuming()