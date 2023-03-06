import pika

# establish a connection to RabbitMQ
connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

# declare a queue
channel.queue_declare(queue='letterbox')

# send a message
message = 'this is my first message'
channel.basic_publish(exchange='', routing_key='letterbox', body=message)
print(f'sent message :{message}')

# close the connection
connection.close()
