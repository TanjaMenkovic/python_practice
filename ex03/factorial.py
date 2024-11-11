def factorial(n: int) -> int:
    result: int = 1

    for i in range(1, n + 1):
        result *= i

    return result

input_num = input("write a number: ")

try:
    num: int = int(input_num)

    if num < 0:
        print("Error: number needs to be positive!")
    else:
        res: int = factorial(num)
        print(f"{num}! = {res}")

except:
    print("Error: Invalid input!")