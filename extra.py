lst = [1, 2, 3]
my_str = "string"
my_int = 123

my_str = my_str.capitalize()
print(my_str)

# all list, string and even integer is of type - class 
print(type(lst))
print(type(my_str))
print(type(my_int))

lst = [1, 2, 3]
# function
# a1 = len(lst)
# method
# a2 = user1.menu()

# from sklearn import LinearRegression
from oops_proj import chatbook

user1 = chatbook()
# print(user1.__name)

# Accessing private attribute using name mangling
# python does not allow direct access to private attributes
# but we can access it using the class name and the attribute name, so it's doesn't completely keeps private
print(user1._chatbook__name)

# getter and setter methods
print(user1.get_name())
user1.set_name("New Chatbook")
print(user1.get_name())


# static variable
print(user1.id)

# using static methods to access and modify static variable
chatbook.set_id(200)
user2 = chatbook()
print(user2.id)
user3 = chatbook()
print(user3.id)
