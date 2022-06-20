def translate(word1,word2):
    list_w1=list(word1)
    list_w2=list(word2)
    list_w2.reverse()
    if list_w2 == list_w1:
        return("YES")
    else:
        return("NO")

word1 = str(input())
word2 = str(input())

print(translate(word1,word2))