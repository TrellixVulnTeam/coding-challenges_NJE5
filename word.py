def capitalize(word):
    upper = 0
    lower = 0
    for letter in word:
        if letter.isupper():
            upper += 1
        elif letter.islower():
            lower += 1
    if lower >= upper:
        return(word.lower())
    elif upper > lower:
        return(word.upper())
    else:
        return(0)

print(capitalize(str(input())))