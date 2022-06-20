def helpful_maths(expression):
    operators = ['+']
    numbers = []
    for number in expression:
        if number not in operators:
            numbers.append(number)
    numbers.sort()
    expression =''
    for i in numbers:
        expression = expression + '+' + i
    print(expression[1:len(expression)])

expression=str(input())

if len(expression) > 0:
    helpful_maths(expression)