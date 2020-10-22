def fibonancci(n):
   # n = int(input("Enter the value : "))

    a = 0
    b = 1
    sum = 0
    count = 1
    result = []
    result.append(a)
    while (count < n):

        #print(sum, end = " ")
        result.append(b)
        count += 1

        a,b = b, a+b
        #a = b
        #b = sum
        #sum = a+b

    return  result