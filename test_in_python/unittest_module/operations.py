def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiplay(a,b):
    return a*b

def division(a,b):
    if b == 0:
        raise ZeroDivisionError("cant divide by zero!!!")
    return a/b