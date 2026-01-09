num = int(input("Enter the term of print fibonacci sequance:"))
a,b = 0,1
if num < 0:
    print("Do not print fibonacci of negative number")
if num == 1:
    print(a)
else:
    print("Fibonacci Sequance:")
    print(a,b, end=' ')
    for i in range(2,num):
        c = a + b
        print(c, end=' ')
        a,b = b,c
