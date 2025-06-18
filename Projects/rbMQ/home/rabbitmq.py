import pika
import random


# To make connection with rabbitMQ dashboard
def publish_message(message):
    # To make the connection
    params = pika.URLParameters('amqps://lpjyeaid:nFBKyo4ItBpwsFlWMckRZEWMahbbzI2F@seal.lmq.cloudamqp.com/lpjyeaid')
    connection = pika.BlockingConnection(params)

    # To publish the message through the channel (medium) 
    # and queue to push the messages
    channel = connection.channel()
    channel.queue_declare(queue='My_queue')
    

    # Now to publish the message / sends the message
    channel.basic_publish(
        exchange='',
          routing_key='My_queue',
            body=message
    )

    print(f"Message Published {message}")
    connection.close()