import datetime
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


# def unique_elements(list):
#     unique = []
#     for i in range(len(list)):
#         print("  ")
#         print(f'--- test run {i} ---')
#         print(f'current unique list : {unique}')
#         print(f'testing for {list[i]}')
#         if list[i] in unique:
#             print(f'{list[i]} is already in the list')
#         else: 
#             unique.append(list[i])
#             print(f'adding {list[i]} to the unique list')
#     return unique

# print(unique_elements(order))

# animals = {'cat': 'meow', 'dog': None, 'cow': 'moo'}

# print(animals.values())
# newdict = {}
# for key, value in animals.items():
    
#     if value != None:
#         newdict[key] = value

# print(newdict)
# print(animals)


# x = animals.values()
# for i in x:
#     print (x[i])
# def remove_none(dictnon):
    
#     for i in range(len(dictnon)):
#         print(dictnon)
#         print (len(dictnon))
#         print(i)


# print(remove_none(animals))




# # #######################################
# def filter_func(pair):
#     remove_this = None
#     key, value = pair
#     if value == remove_this:
#         return False
#     else:
#         return True


# def remove_None_online(mylist):
#     f_dict = dict(filter(filter_func, (mylist).items()))
#     return (f_dict)



# print(remove_None_online(animals))







# location = 'Aldgate East'
# date_time = '2022/01/30 11:12'
# def touch_in(location, date_time):
#     newdict = {'entry point': location , 'time' :date_time}
#     return newdict

# print(touch_in(location, date_time))


# ------------CLASSES ------------




# class StringFormatter():

#     def block_caps(self):
#         return self.upper()
        

# subject = StringFormatter()


class Cohort():

    def __init__(self, name, start_date, end_date):

        
        startyear = int(start_date[0:4])
        startmonth = int(start_date[5:7])
        startday = int(start_date[8:10])
        endyear = int(end_date[0:4])
        endmonth = int(end_date[5:7])
        endday = int(end_date[8:10])

        self.name = name
        self.start_date = datetime.date(startyear, startmonth,startday)
        self.end_date = datetime.date(endyear, endmonth, endday)

    def calculate_duration(self):
        duration = self.end_date - self.start_date
        print(type(duration))
        string_duration = str(duration)
        int_duration = string_duration[0]
        return int_duration

subject = Cohort('January 2060', '2060-01-01', '2060-01-08')


print(subject.calculate_duration())