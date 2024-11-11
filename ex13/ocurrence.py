def count_occurrence(lst: list, element: int) -> int:
    return lst.count(element)

try:
    input_data: str = input("Enter numbers separated by space: ")
    numbers: int = list(map(int, input_data.split()))

    input_num: str = input("Enter a number: ")
    num: int = int(input_num)

    result: int = count_occurrence(numbers, num)
    print("Result: ", result)

except ValueError:
    print("Error: Please enter a valid list of numbers separated by spaces!")