def find_largest(lst: list) -> int:
    return max(lst)

try:
    input_data: str = input("Enter numbers separated by space: ")
    numbers: int = list(map(int, input_data.split()))

    result: int = find_largest(numbers)

    print(f"Largest number in list {numbers} is {result}")

except ValueError:
    print("Error: Please enter a valid list of numbers separated by spaces!")