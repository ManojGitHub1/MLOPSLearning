# initialize a class
class employee:
    # constructor
    # special method/magic method/dunder method
    def __init__(self, name, age):

        # self is a reference to the current instance of the class
        # it is used to access variables that belong to the class
        # id func is used to get the memory address of the object
        print(id(self))
        # attributes
        self.id = 50000
        self.name = name
        self.age = age
        self.designation = "Software Engineer"

    # method/func
    def travel(self, destination):
        print("Traveling to:", destination)


# create an object of the class
sam = employee("Sam", 30)
ram = employee("Ram", 25)

# creating attribute dynamically outside the constructor
# this is not a good practice, but it is allowed in python
sam.gender = "Male"
print(sam.gender)

# id of sam and self is same because self refers to the current instance of the class
# self is the object itself, so object is only allowed to access its own attributes and methods
# object is by default passed as an argument to the method and to access attribute
print(id(sam))
print(id(ram))
# print(sam.id, sam.age)
# print(sam.designation)

# sam.travel("Pune")

