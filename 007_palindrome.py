def next_palindrome(n):
    n = n+1
    while not is_palindrome(n):
        n += 1
    return(n)

def is_palindrome(n):
    return str(n) == str(n)[::-1]


n = int(input("Enter the number of test cases: \n"))
numbers = []

for i in range(n):
    numb = int(input("Enter the number: \n"))
    numbers.append(numb)

# print(numbers)

for i in range(n):
    print(f"Next palindrome of {numbers[i]} is {next_palindrome(numbers[i])}")