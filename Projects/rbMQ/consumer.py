# Consume the messsages produced by Producer

import pika
import pandas as pd
import json
import uuid

def generateExcel(message):
    message = json.loads(message)
    df = pd.DataFrame(message)

    # Generates only 1 file
    # df.to_excel('output.xlsx', index=False)

    # It generates multiple files for every output in queue
    df.to_excel(f'output_{uuid.uuid4()}.xlsx', index=False)

# output
def callback(ch, method, properties, body):
    # print(ch, method, properties, body)
    message = body.decode()
    generateExcel(message)


# Now, we have to bind this 'callback' function 
# Like when we produce the message in rabbitmq then 
# This function should call immediately...

# So, make the connection first
params = pika.URLParameters('amqps://lpjyeaid:nFBKyo4ItBpwsFlWMckRZEWMahbbzI2F@seal.lmq.cloudamqp.com/lpjyeaid')
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='My_queue')

# Now bind 
channel.basic_consume(queue='My_queue', on_message_callback=callback, auto_ack=True)
print("Consumer Started : ")
channel.start_consuming()