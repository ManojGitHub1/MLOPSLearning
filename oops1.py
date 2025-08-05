# initialize a class
class employee:
    # constructor
    # special method/magic method/dunder method
    def __init__(self, name, age):
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
print(sam.id, sam.age)
print(sam.designation)

sam.travel("Pune")

