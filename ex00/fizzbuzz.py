input_data: str = input("Enter numbers separated by space: ")

try:
    numbers: int = list(map(int, input_data.split()))

    result: list = []
    for num in numbers:
        if num % 3 == 0 and num % 5 == 0:
            result.append("fizzbuzz")
        elif num % 3 == 0:
            result.append("fizz")
        elif num % 5 == 0:
            result.append("buzz")
        else:
            result.append(str(num))

    print("Result: ", result)

except ValueError:
    print("Error: Please enter a valid list of numbers separated by spaces!")
