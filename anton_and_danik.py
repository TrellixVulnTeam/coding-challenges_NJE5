def calculate_victory(results):
    results.upper
    count_A = 0
    count_D = 0
    for char in results:
        if char == 'A':
            count_A += 1
        elif char == 'D':
            count_D += 1
    
    if count_A == count_D:
        print("Friendship")
    elif count_A > count_D:
        print("Anton")
    else:
        print("Danik")

matches = int(input())
results = str(input())
if matches == len(results):
    calculate_victory(results)