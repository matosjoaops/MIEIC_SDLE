import zmq
import sys
from random import randrange

type_zipcode = str(sys.argv[1])

upper_limit = 0
port = ""

if type_zipcode == "US":
    upper_limit = 100000
    port = "5556"
else:
    upper_limit = 10000
    port = "5557"

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind(f"tcp://*:{port}")

while True:
    zipcode = randrange(1, upper_limit)
    temperature = randrange(-80, 135)
    relhumidity = randrange(10, 60)

    socket.send_string(f"{zipcode} {temperature} {relhumidity}")