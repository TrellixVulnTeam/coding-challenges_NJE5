def compute_division_sum(n : int) -> int:
    # to-do
    
    sum = 0
    
    for i in range(n+1):
        if i >=5:
            if i % 5 == 0:
                sum = sum + i
            elif i % 7 == 0:
                sum = sum + i
    
    return sum

print(compute_division_sum(5))