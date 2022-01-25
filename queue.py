def create(n):
    queue = [] * n
    return queue

def isempty(queue):
    return len(queue) == 0

def isfull(queue, n):
    return len(queue) == n

def enqueue(queue, item):
    queue.append(item)

def dequeue(queue):
    if len(queue)!=0:
        queue.pop(0)

n=3
a = create(n)
print(isempty(a))
enqueue(a,1)
enqueue(a,2)
enqueue(a,3)
print(a)
print(isfull(a,n))
dequeue(a)
print(isfull(a,n))
dequeue(a)
print(a)
print(isempty(a))
dequeue(a)
print(isempty(a))