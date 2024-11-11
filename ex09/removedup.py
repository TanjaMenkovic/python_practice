def remove_duplicates(lst: list) -> list:
    return list(set(lst))

try:
    input_data: str = input("Enter numbers separated by space: ")
    numbers: int = list(map(int, input_data.split()))

    result: list = remove_duplicates(numbers)
    print("After removing duplicates from list, we get: ", result)

except ValueError:
    print("Error: Please enter a valid list of numbers separated by spaces!")
