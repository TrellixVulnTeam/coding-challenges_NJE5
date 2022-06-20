def boy_or_girl(name):
    unique_letters = set(name)
    if len(unique_letters) % 2 == 0:
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")

name=str(input())
boy_or_girl(name)