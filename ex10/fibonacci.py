def fibonacci(n: int) -> list:
    fib_sequence = [0, 1]

    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    return fib_sequence

input_num: str = input("Write a number: ")

try:
    num: int = int(input_num)
    
    print(f"Fibonacci sequence for number '{num}' is: {fibonacci(num)}")

except:
    print("Error: Invlaid input!")