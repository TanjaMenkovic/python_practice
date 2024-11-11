def is_palindrome(s: str) -> bool:
    s = s.replace(" ", "").lower()

    if s == s[::-1]: # s[start:end:step]
        return True
    else:
        return False

word = input("Enter a sequence of letters: ")

if is_palindrome(word):
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' isn't a polindrome.")