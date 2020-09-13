food_calories=list(map(int,input().split(',')))
#method1
food_calories.reverse()
print(food_calories)
#method2
food_calories[::-1]
print(food_calories)
#method3

# for i in range((len(food_calories))):
#     temp=food_calories[i]
#     food_calories[i]=food_calories[-1+-i]
#     food_calories[-i+-1]=temp
# print(food_calories)
#
# if __name__ == '__main__':
