def is_palindrome(input: str) -> bool:
    # to-do
    for i in range(len(input)+1):
        if input[i-1] != input[-i]:
            return False
    return True

print(is_palindrome("anna"))