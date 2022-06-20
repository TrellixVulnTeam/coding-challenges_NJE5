def get_fibonacci(n : int) -> int:
    # to-do
    fibo = 0
    previous = 0
    f_index = 0
    for i in range(1,n):
        if i > 2:
            fibo = i + previous
        elif i == 0:
            fibo = 0
        else:
            fibo = 1
        
        previous = i
    return fibo

print(get_fibonacci(3))