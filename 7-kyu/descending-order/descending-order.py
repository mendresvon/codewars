def descending_order(num):
    num = list(str(num))
    num.sort(reverse=True)
    num = ''.join(num)
    return int(num)