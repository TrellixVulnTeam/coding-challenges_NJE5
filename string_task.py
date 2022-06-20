def string_task(word):
    vowels = ['a','e','i','o','u','y']
    consoants = ''
    for letter in word:
        if letter not in vowels:
            consoants = consoants + '.' + letter
    print(str(consoants))

word=str(input())

if len(word) > 0:
    string_task(word.lower())