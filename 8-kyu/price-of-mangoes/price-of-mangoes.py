def mango(quantity, price):
    free = quantity // 3
    not_free = quantity - free
    return not_free * price