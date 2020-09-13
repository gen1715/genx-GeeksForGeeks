'''
Task

You are given two values  and .
Perform integer division and print .

Input Format

The first line contains , the number of test cases.
The next  lines each contain the space separated values of  and .

Constraints

Output Format

Print the value of .
In the case of ZeroDivisionError or ValueError, print the error code.

Sample Input

3
1 0
2 $
3 1
Sample Output

Error Code: integer division or modulo by zero
Error Code: invalid literal for int() with base 10: '$'
3
Note:
For integer division in Python 3 use //.
'''

n = int(input())
for i in range(0,n):
    try:
        a,b=map(int,input().split())
        print(a//b)
    except Exception as e:
        print ("Error Code:",e)
