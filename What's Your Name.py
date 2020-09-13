def print_full_name(first_name,last_name):
    check = { True : 'Ok to prceed', False : 'Please reenter name with 10 characters'}
    result = (check[len(first_name) < 10 and len(last_name) < 10])
    if result == 'Ok to prceed':
        print(f"Hello {first_name} {last_name}! You just delved into python.")
    else:
        print(check[len(first_name) < 10 and len(last_name) < 10])
if __name__=='__main__':
   print("Please enter first name :")
   first_name = input()
   print("Please enter Last name :")
   last_name = input()
   print_full_name(first_name, last_name)

