import time

from random import randint
from string import ascii_uppercase as uppercase
from threading import Thread

import zmq
from zmq.devices import monitored_queue

from zhelpers import zpipe

def subscriber_thread():
    ctx = zmq.Context().instance()
    
    
    subscriber = ctx.socket(zmq.SUB)
    subscriber.connect("tcp://localhost:6001")
    subscriber.setsockopt(zmq.SUBSCRIBE, b"A")
    subscriber.setsockopt(zmq.SUBSCRIBE, b"B")
    
    count = 0
    while count < 5:
        try:
            msg = subscriber.recv_multipart()
        except zmq.ZMQError as e:
            