def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
        
    return True

input_num: str = input("Write a number: ")

try:
    num: int = int(input_num)
    if is_prime(num):
        print(f"'{num}' is a prime number")
    else:
        print(f"'{num}' is not a prime number")

except:
    print("Error: Invlaid input!")