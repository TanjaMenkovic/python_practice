def sum_of_dig(n: int) -> int:
    return sum(int(digit) for digit in str(n))

input_num: str = input("Write a number: ")

try:
    num: int = int(input_num)
    sum_dig: int = sum_of_dig(num)

    print(f"Sum of digits of number {num} is {sum_dig}")

except:
    print("Error: Invlaid input!")