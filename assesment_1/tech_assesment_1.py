def series_of_number(input):
    a = 2
    res =[]
    for i in range (int(input)):
        res.append(str(a))
        a += 3
    print (",".join(res))


a = input("Insert number: ")
series_of_number(a)