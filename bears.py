def years_to_become_larger(bear1, bear2):
    years = 0
    while bear1 <= bear2:
        bear1 += 2*bear1
        bear2 += bear2
        years += 1
    return(years)


bear1,bear2 = map(int,input().split())
print(years_to_become_larger(bear1,bear2))