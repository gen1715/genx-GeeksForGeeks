def next_palindrome(n):
    n = n+1
    while not is_palindrome(n):
        n += 1
    return(n)

def is_palindrome(n):
    return str(n) == str(n)[::-1]


size = int(input("ënter the number \n "))
num_list = []
for i in range(size):
    num_list.append(int(input("Enter the number to add in list \n")))
print(num_list)

next_list = []
for i in range(len(num_list)):
    t = next_palindrome(num_list[i])
    next_list.append(t)

print (next_list)