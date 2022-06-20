def problems_to_solve(problems):
    solve_capacity=0
    for problem in problems:
        sum=0 
        j = 0
        while j < len(problem):
            sum = sum + int(problem[j])
            j += 1
        if sum > 1:
            solve_capacity += 1
    print(solve_capacity)


number_of_problems = int(input())
i=0
problems = []
while (i  < number_of_problems):
    petya,vasya,tonya = map(int,input().split())
    problems.append([petya,vasya,tonya])
    i += 1

problems_to_solve(problems)


