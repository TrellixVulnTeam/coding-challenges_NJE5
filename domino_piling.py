def domino_piling(m,n):
    if n % 2 ==0 and m % 2 ==0:
        print((n//2) * m)
    elif n % 2 == 0 :
        print((n//2) * m)
    elif m % 2 == 0 :
        print((m//2) * n)
    else:
        print(((n//2) * m) + m//2)


n,m = map(int,input().split())
domino_piling(m,n)