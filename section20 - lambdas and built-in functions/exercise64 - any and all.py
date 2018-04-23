# Implement your is_all_strings function below:
def is_all_strings(lst):
    return all(type(l) == str for l in lst)


print(is_all_strings(['1', '2', 'hbh']))