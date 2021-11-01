import threads.PutThread

def put(topic, message):
    # how to check if a publisher already exists for the topic?
    thread = threads.PutThread(topic, message)