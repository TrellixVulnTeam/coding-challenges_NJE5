def reverse(input: str) -> str:
    # to-do
    new_string = ""
    for i in range(1,len(input)+1):
        new_string = new_string + input[-i]
    if new_string == "":
        return "You Have Inputted an Out of Bounds Value."
    return new_string
    
print(reverse("juliano"))