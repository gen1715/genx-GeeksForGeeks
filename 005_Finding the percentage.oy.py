
n = int(input())
dic = {}
for _ in range(n):
    stat = [i for i in input().strip().split(' ')]

    ### map needed to be cast as list because there is a data type as map in python3. len(marks) will throw error.

    marks = list(map(float, stat[1:]))

    dic[stat[0]] = sum(marks)/len(marks)
print('{0:.2f}'.format(dic[input()]))



# # python 3 code stub
# if __name__ == '__main__':
#     n = int(input())
#     # dictionary to store the marks, key = name, value = list of scores
#     student_marks = {}
#     # read in all the records and store in the dictionary
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     # query_name is the key value to retrieve
#     query_name = input()
# #
# # divide the sum of the scores list by the length of the scores list
# # format to 2 places after the decimal and print to STDOUT
# #
# # the solution:
# #
# print('{0:.2f}'.format(sum(student_marks[query_name])/len(student_marks[query_name])))