def are_anagrams(a : str, b : str) -> bool:
    # to-do
    matches = 0
    for letter_in_a in a:
        if letter_in_a in b:
            matches+=1
    if matches==len(a):
        return True
    return False

are_anagrams("rio","ior")