def valid_numb(a, b):
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("а должен быть int или float")
    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("b должен быть int или float")

def add(a, b):
    valid_numb(a, b)
    return a + b


def subtract(a, b):
    valid_numb(a, b)
    return a - b


def multiply(a, b):
    valid_numb(a, b)
    return a * b


def divide(a, b):
    valid_numb(a, b)
    if b == 0:
        raise ZeroDivisionError("на ноль делить нельзя")
    return a / b


