def fib(max):
    n, a, b = 0, 0, 1
    print(0)
    while n < max-1:
        print(b)
        a, b = b, a + b
        n = n + 1
while True:
    print(fib(int(input(Enter A Number:))))
