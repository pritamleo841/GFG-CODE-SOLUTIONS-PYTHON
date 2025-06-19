'''
    :param x: value to be inserted
    :return: None

    queue_1 = Queue() # first queue
    queue_2 = Queue() # second queue
   '''
from queue import Queue
queue_1=Queue()
queue_2=Queue()
def push(x):
    global queue_1,queue_2
    #Enqueue x to queue_2
    queue_2.put(x)
    #Move all elements from queue_1 to queue_2
    while not queue_1.empty():
        queue_2.put(queue_1.get())
    #Swap queue_1 and queue_2
    queue_1,queue_2=queue_2,queue_1

def pop():
    global queue_1, queue_2

    if not queue_1.empty():
        return queue_1.get()
    else:
        return -1