from logging import NullHandler
import pika
import pageviewapi 
from datetime import datetime

from six import viewitems


def obtenerFecha():
    fechaA = str(datetime.today().strftime('%Y-%m-%d'))

    fechaA = ''.join( x for x in fechaA if x not in "-")

    return fechaA



connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

#El consumidor utiliza el exchange 'log'
channel.exchange_declare(exchange='logs', exchange_type='fanout')

#Se crea un cola temporaria exclusiva para este consumidor (búzon de correos)
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

#La cola se asigna a un 'exchange'
channel.queue_bind(exchange='logs', queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r" % body)
    busqueda = body.decode('utf-8')
    busqueda = busqueda[16:len(busqueda)-1]
    print("Numero de visitas desde 01/01/2021 hasta la fecha ")
    fechaA = obtenerFecha()
    v =  pageviewapi.per_article('en.wikipedia', busqueda, '20000101', fechaA, access='all-access', agent='all-agents', granularity='daily')
    n = 0

    for  i in  v["items"]:
        n += i["views"]
    print(n)


channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()