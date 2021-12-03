import zmq
from random import randrange

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.connect("tcp://localhost:5560")

while True:
    zipcode = randrange(1, 100000)
    temperature = randrange(-80, 135)
    relhumidity = randrange(10, 60)

    socket.send_string(f"{zipcode} {temperature} {relhumidity}")