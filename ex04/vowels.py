def count_vowels(s: str) -> int:
    vowels: str = "aeiou"
    count: int = 0

    for char in s:
        if char.lower() in vowels:
            count += 1
    
    return count

s: str = input("Write an input: ")

c: int = count_vowels(s)
print(f"{c} is number of vowels in '{s}'")
