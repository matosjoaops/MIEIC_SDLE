import sys
import time
import zmq
from threading import Thread

from zmq.sugar import socket

class PutThread(Thread):
    def __init__(self, topic, message):
        Thread.__init__(self)
        self.topic = topic
        self.message = message

    def run(self):
        context = zmq.Context()
        socket = context.socket(zmq.PUB)
        socket.bind("tcp://*:5556")

        while True: