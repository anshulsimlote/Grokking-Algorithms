queueImp = []

def enqu(val):
    queueImp.append(val)

def deq():
    if queueImp:  # check if not empty
        return queueImp.pop(0)
    return None  # or raise an exception

print(f"Queue: {queueImp}")
enqu(1)
enqu(2)
print(f"Queue: {queueImp}")
print(f"Dequeued: {deq()}")
print(f"Queue: {queueImp}")
