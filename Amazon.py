# What is the
# output
# of
# the
# Python
# code
# given
# below:


def extendList(val, list=[]):
    list.append(val)
    return list

list3 = extendList('a')
list1 = extendList(10)
list2 = extendList(123, [])


print("list1 = %s" % list1)
print("list2 = %s" % list2)
print("list3 = %s" % list3)

# list1 = [10]
# list2 = [123]
# list3 = [a]
