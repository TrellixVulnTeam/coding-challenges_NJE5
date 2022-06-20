def bit_plus(n, X):
    finalValue = 0
    for operators in X:
        if operators == '++X' or operators == 'X++':
            finalValue += 1
        elif operators == '--X' or operators == 'X--':
            finalValue -= 1
        else:
            print("Wrong Operator: {}".format(operators))
    print(finalValue)


n = int(input())
X = []
i = 0
while i < n:
    X.append(str(input()))
    i += 1

bit_plus(n, X)
