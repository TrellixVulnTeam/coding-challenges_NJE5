def abreviatte(words):
    for word in words:
        if len(word) <= 10:
            print(word)
        elif len(word) > 10:
            print("{}{}{}".format(word[0],len(word)-2,word[len(word)-1]))

number_of_words = int(input())
words = []
i=0
if number_of_words > 0 and number_of_words <= 100:
    while i < number_of_words:
        words.append(input())
        i += 1

    abreviatte(words)