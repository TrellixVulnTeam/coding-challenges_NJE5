def stones_on_the_table(stones):
    i = 1
    neighbours = 0
    while i < len(stones):
        if stones[i] == stones[i-1]:
            neighbours += 1
        i += 1
    print(neighbours)

size=int(input())
stones=str(input())
if size == len(stones):
    stones_on_the_table(stones)