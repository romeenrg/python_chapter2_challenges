# list = [2, 5, 3, 1, 4, -1, 2, -4, -100]

# def lowest_number(mylist):
#     lownumber = 0
#     for i in range(len(mylist)):
#         print('--- start of test ----')
#         print (f'loop {i}')
#         print (f'lowest number right now is {lownumber}')
#         print (f'testing again {mylist[i]}')

#         if i == 0:
#             lownumber = mylist[i]
            
#         elif lownumber > mylist[i]:
#             lownumber = mylist[i] 

#     return f'lowest number is {lownumber}'


# print(lowest_number(list))


# def the_beatles():
#     return ['john', 'paul', 'george', 'ringo']
# print(the_beatles())


# def i_joined_the_beatles(name):
#     beatles = ['john', 'paul', 'george', 'ringo']
#     beatles.append(name)
#     return beatles

# print(i_joined_the_beatles('romeen'))

order  = [1, 3, 2, 6, 1, 7, 8, 8, 8]

# def remove_nones_from_list(list):
#     nonelist = []
#     for i in range(len(list)):
#         print('  ')
#         print(f'--- test run {i} ---')
#         print(f'testing list {list[i]}')
        
#         if list[i] != None:
#             nonelist.append(list[i])

#     return nonelist

# print(remove_nones_from_list(list))


def unique_elements(list):
    unique = []
    for i in range(len(list)):
        print("  ")
        print(f'--- test run {i} ---')
        print(f'current unique list : {unique}')
        print(f'testing for {list[i]}')
        if list[i] in unique:
            print(f'{list[i]} is already in the list')
        else: 
            unique.append(list[i])
            print(f'adding {list[i]} to the unique list')
    return unique

print(unique_elements(order))