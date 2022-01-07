def fibonacci(limit):
    a1 = 0
    a2 = 0
    a3 = 1
    b = ""
    for x in range(limit):
        b = str(b) + " " + str(a2)
        a1 = a2
        a2 = a3
        a3 = a1 + a2
    return b


k = input("Please Enter the limit:-")
result = fibonacci(int(k))
print(result)
