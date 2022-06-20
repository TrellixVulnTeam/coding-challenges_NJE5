def next_round(n,k,scores):
    scores.sort()
    scores.reverse()
    maximum_score = scores[0]+1
    minimum_score = scores[k-1]
    finalists = 0
    for score in scores:
            if score in range(minimum_score, maximum_score) and score > 0:
                finalists += 1
    print(finalists)


print(9//2)
#n,k = map(int,input().split())
#scores = list(map(int,input().split()))
#next_round(n,k,scores)