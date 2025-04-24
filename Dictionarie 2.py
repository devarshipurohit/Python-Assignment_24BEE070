def is_dict_empty(d):
    return not bool(d)

empty_dict = {}
non_empty_dict = {'key': 'value'}

print("Is empty_dict empty?", is_dict_empty(empty_dict))     # True
print("Is non_empty_dict empty?", is_dict_empty(non_empty_dict))  # False
