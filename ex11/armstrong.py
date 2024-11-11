def is_armstrong(n: int) -> bool:
    num_str: str = str(n)
    num_digits: int = len(num_str)
    sum_of_powers: int = sum(int(digit) ** num_digits for digit in num_str)
    
    return sum_of_powers == n

input_num: str = input("Write a number: ")

try:
    num: int = int(input_num)
    if is_armstrong(num) == True:
        print(f"Number {num} is Armstrong number")
    else:
        print(f"Number {num} isn't Armstrong number")

except:
    print("Error: Invlaid input!")