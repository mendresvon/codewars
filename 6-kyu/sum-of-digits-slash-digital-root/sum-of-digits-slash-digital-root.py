def digital_root(n):
    num = n
    res = 0
    while True:
        curr_sum = 0
        while n != 0:
            curr_sum += n % 10
            n //= 10
        if curr_sum < 10:
            res = curr_sum
            break
        n = curr_sum
    return res