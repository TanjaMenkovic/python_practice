def reverse_list(lst: list) -> list:
    return lst[::-1]

try:
    input_data: str = input("Enter numbers separated by space: ")
    numbers: int = list(map(int, input_data.split()))

    result: list = reverse_list(numbers)

    print("Result: ", result)

except ValueError:
    print("Error: Please enter a valid list of numbers separated by spaces!")