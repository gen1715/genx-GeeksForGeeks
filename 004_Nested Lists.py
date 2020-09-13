# if __name__ == '__main__':
#     #for _ in range(int(input())):
#     #    name = input()
#     #    score = float(input())
#     marksheet = []
#     for _ in range(0,int(input())):
#         marksheet.append([input(), float(input())])
#     #print(marksheet)
#     second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
#     #print (second_highest)
#     print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))

if __name__ == '__main__':
    score_list = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score in score_list:
            score_list[score].append(name)
        else:
            score_list[score] = [name]
    print(score_list)
    new_list = []
    for i in score_list:
         new_list.append([i, score_list[i]])

    new_list.sort()
    print(score_list)
    result = new_list[1][1]
    print(result)
    result.sort()
    print(result)
    print (*result, sep = "\n")