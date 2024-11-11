def even_or_odd(n: int) -> str:
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

input_num: str = input("Write a number: ")

try:
    num: int = int(input_num)
    print("Number is: ", even_or_odd(num))

except:
    print("Error: Invlaid input!")