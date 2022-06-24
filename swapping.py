def swapData():
    file1 = input("Your file: ")
    file2 = input("Get file: ")

    with open(file1, 'r') as a:
        data_a = a.read()
    with open(file2, 'r') as b:
        data_b = b.read()

    print(data_a)
    print(data_b)
    
    with open(file1, 'w') as a:
        a.write(data_b)
    with open(file2, 'w') as b:
        b.write(data_a)

    print(data_a)
    print(data_b)

swapData()