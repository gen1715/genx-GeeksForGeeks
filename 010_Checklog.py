def is_alnum(st):
    return(st.isalnum())

def is_lower(st):
    return(st.islower())

def is_digit(st):
    return(st.isnumeric())

instr = input()

print(is_alnum(instr))
print(is_lower(instr))

print(is_digit(instr))