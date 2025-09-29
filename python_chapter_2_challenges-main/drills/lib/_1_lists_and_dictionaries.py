# == INSTRUCTIONS ==
#
# In these exercises you will define your own functions.
#
# Most functions will take a list or a dictionary as an argument, but some will
# take other arguments and some won't take any.
#
# The requirements will always start with the name of the function. Use this
# name exactly or the tests won't be able to find it.
#
# Then there will be a description of what the function should do. Note that
# some solutions will require more than one line of code.
#
# You won't find everything that you need in our materials. Use the Python Docs
# and Google liberally if you get stuck.

# == LIST EXERCISES ==

# Method name: first_element
# Purpose: returns the first element of the given list
# Arguments: one list
# Example:
#   Call:    first_element([1, 2, 3])
#   Returns: 1

def first_element(my_list):
    return my_list[0]


# Method name: second_element
# Purpose: returns the second element of the given list
# Arguments: one list
# Example:
#   Call:    second_element([1, 2, 3])
#   Returns: 2
def second_element(my_list):
    return my_list[1]


# Method name: last_element
# Purpose: returns the last element of the given list
# Arguments: one list
# Example:
#   Call:    last_element([1, 2, 3])
#   Returns: 3
def last_element(my_list):
    return my_list[-1]


# Method name: first_two_elements
# Purpose: returns the first two elements of the given list
# Arguments: one list
# Example:
#   Call:    first_two_elements([1, 2, 3])
#   Returns: [1, 2]
def first_two_elements(my_list):
    return my_list[0:2]


# Method name: first_three_elements
# Purpose: returns the first three elements of the given list
# Arguments: one list
# Example:
#   Call:    first_three_elements([1, 2, 3, 4])
#   Returns: [1, 2, 3]
def first_three_elements(my_list):
    return my_list[0:3]


# Method name: total
# Purpose: returns the sum of all the elements in the given list
# Arguments: one list
# Example:
#   Call:    total([1, 2, 3])
#   Returns: 6


def total(mylist):
    ans = 0
    for i in range(len(mylist)):
        ans = ans + mylist[i]
    return ans

# Method name: lowest_number
# Purpose: returns the lowest number in the given list
# Arguments: one list
# Example:
#   Call:    lowest_number([4, 2, 6])
#   Returns: 2

def lowest_number(mylist):
    lownum = 0 
    for i in range(len(mylist)):
        if i == 0:
            lownum = mylist[i]

        elif lownum > mylist[i]:
            lownum = mylist[i]

    return lownum

# Method name: highest_number
# Purpose: returns the highest number in the given list
# Arguments: one list
# Example:
#   Call:    highest_number([4, 6, 2])
#   Returns: 6
def highest_number(mylist):
    highnum = 0 
    for i in range(len(mylist)):
        if i == 0:
            highnum = mylist[i]
        elif highnum < mylist[i]:
            highnum = mylist[i]
        
    return highnum


# Method name: the_beatles
# Purpose: returns the list ['john', 'paul', 'george', 'ringo']
# Arguments: none
# Example:
#   Call:    the_beatles()
#   Returns: ['john', 'paul', 'george', 'ringo']
def the_beatles():
    return ['john', 'paul', 'george', 'ringo']

# Method name: i_joined_the_beatles
# Purpose: adds the given name to the list ['john', 'paul', 'george', 'ringo']
# Arguments: one string
# Example:
#   Call:    i_joined_the_beatles('yoko')
#   Returns: ['john', 'paul', 'george', 'ringo', 'yoko']

def i_joined_the_beatles(name):
    beatles = ['john', 'paul', 'george', 'ringo']
    beatles.append(name)
    return beatles

# Method name: we_joined_the_beatles
# Purpose: adds the given names to the list ['john', 'paul', 'george', 'ringo']
# Arguments: one list
# Example:
#   Call:    we_joined_the_beatles(['yoko', 'stuart'])
#   Returns: ['john', 'paul', 'george', 'ringo', 'yoko', 'stuart']
def we_joined_the_beatles(list):
    beatles = ['john', 'paul', 'george', 'ringo']
    for i in range(len(list)):
        beatles.append(list[i])
    return beatles



# Method name: remove_nones_from_list
# Purpose: removes all the None values from the given list
# Arguments: one list
# Example:
#   Call:    remove_nones_from_list([1, None, 2, None, 3])
#   Returns: [1, 2, 3]

def remove_nones_from_list(list):
    nonelist = []
    for i in range(len(list)):
        if list[i] != None:
            nonelist.append(list[i])

    return nonelist


# Method name: double_list
# Purpose: returns a list with all the elements of the given list repeated twice
# Arguments: one list
# Example:
#   Call:    double_list([1, 2, 3])
#   Returns: [1, 2, 3, 1, 2, 3]

def double_list(list):
    for i in range(len(list)):
        list.append(list[i])
    return list


# Method name: unique_elements
# Purpose: returns a list with all the unique elements of the given list
# Arguments: one list
# Example:
#   Call:    unique_elements([1, 2, 1, 3, 2, 3])
#   Returns: [1, 2, 3]

def unique_elements(list):
    unique = []
    for i in range(len(list)):
        if list[i] in unique:
            unique
        else: 
            unique.append(list[i])
    return unique



# Method name: add_to_list
# Purpose: adds the given element to the given list
# Arguments: one list and one element
# Example:
#   Call:    add_to_list(["a", "b", "c"], "d")
#   Returns: ["a", "b", "c", "d"]

def add_to_list(list, value):
    list.append(value)
    return list


# == DICTIONARY EXERCISES ==

# Method name: new_band_member
# Purpose: merges a given dictionary into an existing dictionary
# Arguments: one dictionary
# Note: {"vocalist": "miss piggy", "lead_guitar": "scooter"}
# Example:
#   Call:    new_band_member({"bass": "flea"})
#   Returns: {"vocalist": "miss piggy", "lead_guitar": "scooter", "bass": "flea"}

def new_band_member(newdict):
    dict = {'vocalist' : 'miss piggy', 'lead_guitar':'scooter',}
    dict.update(newdict)
    
    return dict


# Method name: all_values
# Purpose: returns a list of all the values in the given dictionary
# Arguments: one dictionary
# Example:
#   Call:    all_values({"a": 1, "b": 2, "c": 3})
#   Returns: [1, 2, 3]
def all_values(dict):
    return dict.values()


# Method name: all_keys
# Purpose: returns a list of all the keys in the given dictionary
# Arguments: one dictionary
# Example:
#   Call:    all_keys({"a": 1, "b": 2, "c": 3})
#   Returns: ["a", "b", "c"]
def all_keys(dict):
    return dict.keys()

# Method name: remove_nones_from_dictionary
# Purpose: removes all pairs from a given dictionary where the value is None
# Arguments: one dictionary
# Example:
#   Call:    remove_nones_from_dictionary({"a": 1, "b": None, "c": 3})
#   Returns: {"a": 1, "c": 3}

# def filter_func(pair):
#     remove_this = None
#     key, value = pair
#     if value == remove_this:
#         return False
#     else:
#         return True

    
# def remove_nones_from_dictionary(mylist):
#     f_dict = dict(filter(filter_func, (mylist).items()))
#     return (f_dict)

# animals = {'cat': 'meow', 'dog': None, 'cow': 'moo'}

#      ****done via online help****

def remove_nones_from_dictionary(dict_with_none):
    removed_dict = {}
    for key, value in dict_with_none.items():
        if value != None:
            removed_dict[key] = value
    return removed_dict


# Method name: touch_in
# Purpose: creates a dictionary from a given tube station and time
# Arguments: two strings, one for the tube station and one for the time
# Example:
#   Call:    touch_in('Aldgate East', '2022/01/30 17:12')
#   Returns: {'entrypoint': 'Aldgate East', 'time': '2022/01/30 17:12'}

def touch_in(location, date_time):
    newdict = {'entrypoint': location , 'time' :date_time}
    return newdict