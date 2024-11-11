def sum_in_range(start, end):
    return sum(range(start, end + 1))

try:
    input_nums: str = input("Write 2 numbers separated by space: ")
    numbers: int = list(map(int, input_nums.split()))

    if len(numbers) != 2:
        print("Error: Write 2 numbers only!")
    else:
        result: int = sum_in_range(numbers[0], numbers[1])
        print("Result: ", result)

except:
    print("Error: Invalid input!")
