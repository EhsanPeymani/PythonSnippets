# Dan Bader

my_dict = dict(a=5, c=3, b=10, e=2, d=9)

# sorted will return a list of sorted keys
sorted_dict_1 = sorted(my_dict)
print('sorted(my_dict):', sorted_dict_1)

# sort dictionary by value -- method 1
sorted_dict_2 = sorted(my_dict.items(), key=lambda item: item[1])
print('sorted(my_dict.items(), key=lambda item: item[1]):', sorted_dict_2)
print('dict(sorted(my_dict.items(), key=lambda item: item[1])):', dict(sorted_dict_2))

# sort dictionary by value -- method 2
import operator
sorted_dict_3 = sorted(my_dict.items(), key=operator.itemgetter(1))
print('sorted(my_dict.items(), key=operator.itemgetter(1)):', sorted_dict_3)
print('dict(sorted(my_dict.items(), key=operator.itemgetter(1))):', dict(sorted_dict_3))
