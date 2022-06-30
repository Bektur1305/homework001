def zeros(n):
    counter = 0
    while n > 0:
        n = n // 5
        counter += n
    return counter