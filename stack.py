def create(n):
    stack = [] * n
    return stack


def isempty(stack):
    return len(stack) == 0


def isfull(stack, n):
    return len(stack) == n

def push(stack, item):
    stack.append(item)

def pop(stack):
    if len(stack)!=0:
        stack.pop()

def peek(stack):
    return stack[-1]

n = 3
a = create(n)
push(a, 1)
push(a, 2)
push(a, 3)
print(a)
print(isfull(a, n))
pop(a)
print(peek(a))
print(a)
pop(a)
print(isfull(a, n))
pop(a)
print(isempty(a))
print(a)
