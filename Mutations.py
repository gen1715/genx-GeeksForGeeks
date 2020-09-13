def mutate_string(string, position, character):
    out = list(string)
    out[position] = character
    stringnew = ''.join(out)
    return stringnew

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)