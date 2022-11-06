import functools

def append(list1, list2):
    new_list = list1 + list2
    return new_list

def concat(lists):
    new_list = []
    for list in lists:
        new_list += list
    return new_list

def filter(function, list):
    return [item for item in list if function(item)]

def length(list):
    counter = 0
    for item in list:
        counter += 1
    return counter

def map(function, list):
    return [function(item) for item in list]

def foldl(function, list, initial):
    result = initial
    for item in list:
        result = function(result, item)
    return result

def foldr(function, list, initial):
    result = initial
    for item in reverse(list):
        result = function(item, result)
    return result

def reverse(list):
    return list[::-1]
