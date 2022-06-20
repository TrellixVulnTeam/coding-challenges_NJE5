def divide_watermelon(weight):
    if weight % 2 == 0 and weight > 2 and weight < 101:
        print("YES")
    else:
        print("NO")

w = int(input())
if w:
    divide_watermelon(w)
else:
    print("NO")