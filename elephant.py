def steps(distance):
    minor = 0
    steps = 0
    if distance // 5 == 0:
        minor = distance // 5
    if distance // 4 == 0:
        minor = distance // 4
    if distance // 3 == 0:
        minor = distance // 3

    steps = distance // 5
    distance = distance % 5
    if distance % 4 == 0:
        steps = steps + (distance // 4)
    distance = distance %4
    if distance % 3 == 0:
        steps = steps + (distance // 3)
    
    print (minor)
    print (steps)

    if steps <= minor:
        return(steps)
    else:
        return(minor)

print(steps(int(input())))