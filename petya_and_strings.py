def petya_and_strngs(string1, string2):
    if string1 > string2:
        print(1)
    elif string1 < string2:
        print(-1)
    else:
        print(0)


string1 = str(input())
string2 = str(input())

if len(string1) <= 100 and len(string1) >0 and len(string2) <= 100 and len(string2) >0:
    petya_and_strngs(string1.upper(), string2.upper())