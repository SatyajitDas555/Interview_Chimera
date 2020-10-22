def fibonancci(n):

    a = 0
    b = 1

    if n <= 0:
        print("Incorrect")
    elif n == 1:
        return b
    else:
        for x in range(2, n):

            c = a+b
            a = b
            b = c
        return b
print(fibonancci(10))


