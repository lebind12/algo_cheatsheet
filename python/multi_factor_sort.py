import sys


example_list = [(21, 'Sam'), (22, 'Adel'), (21, 'Adam'), (22, 'Sol'), (23, 'Mike'), (25, 'Lee')]
# print(sorted(example_list, key=lambda x : x[0]))
# print(example_list)
example_list.sort(key=lambda x : x[0])
print(example_list)
example_list.sort(key=lambda x: x[1], reverse=1)
print(example_list)