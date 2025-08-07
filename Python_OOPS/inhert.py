# # Simple inheritance

# # Base class
# class Animal:
#     def __init__(self, name):
#         self.name = name
#         self.__type = "4-legged"  # Private attribute

#     def speak(self):
#         print(f"{self.name} makes a sound.")

# # Derived class
# class Dog(Animal):

#     # Constructor overriding
#     def __init__(self, name):
#         super().__init__(name)  # Call the constructor of the base class
#         # if not above line is used, it will not initialize the base class attributes
#         # and won't to able to use attr & methods of base class
#         # super().speak()
#         self.breed = "Labrador"

#     def speak(self):
#         super().speak()  # Call the base class method
#         print(f"{self.name} barks & is of breed {self.breed}.")
#         print(f"Type: {self._Animal__type}")  # Accessing private attribute using name mangling

# # Create an instance of Animal
# animal = Animal("Generic Animal")
# # animal.speak()

# # Create an instance of Dog
# dog = Dog("Buddy")
# dog.speak()

# ----------------------------------------------------------------

# Multiple inheritance

# Base class
class Grandparent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I am {self.name} from Grandparent.")

# Intermediate class 1
class Parent1(Grandparent):
    def greet(self):
        print(f"Hello, I am {self.name} from Parent1.")
        super().greet()

# Intermediate class 2
class Parent2(Grandparent):
    def greet(self):
        print(f"Hello, I am {self.name} from Parent2.")
        super().greet()

# Derived class
class Child(Parent1, Parent2):
    def greet(self):
        print(f"Hello, I am {self.name} from Child.")
        Parent1.greet(self)  # Call greet from Parent1
        Parent2.greet(self)  # Call greet from Parent2
        super().greet()  # Call greet from Child

# Create an instance of Child
child = Child("Alice")
child.greet()  # Calls greet from both Parent1 and Parent2


# How it works:

# 1. MRO (Method Resolution Order):
# For Child, the MRO is [Child, Parent1, Parent2, Grandparent, object].

# 2. Cooperative super():
# Child.greet() calls super().greet(), which resolves to Parent1.greet().
# Parent1.greet() prints its line, then calls super().greet(), which resolves to Parent2.greet().
# Parent2.greet() prints its line, then calls super().greet(), which resolves to Grandparent.greet().
# Grandparent.greet() prints the final line.
# By using super() in every override, you ensure each class in the inheritance chain gets its turn to run its version of greet() exactly once, in the proper order.


# -----------------------------------------------------------------

# # Multilevel inheritance

# # Base class
# class Grandparent:
#     def __init__(self, name):
#         self.name = name

#     def tell_stroy(self):
#         print(f"{self.name} tells a stroy.")

# # Intermediate class
# class Parent(Grandparent):
#     def __init__(self, name):
#         super().__init__(name)

#     def work(self):
#         print(f"{self.name} is working.")

# # Derived class
# class Child(Parent):
#     def __init__(self, name):
#         super().__init__(name)

#     def play(self):
#         print(f"{self.name} is playing.")

# # Create an instance of Child
# child = Child("Alice")
# child.tell_stroy()  # From Grandparent
# child.work()       # From Parent    
# child.play()       # From Child

# -----------------------------------------------------------------

# # Hierarchical inheritance

# # Base class
# class Parent:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         print(f"Hello, I am {self.name}.")

# # Derived class 1
# class Child1(Parent):
#     def __init__(self, name):
#         super().__init__(name)

#     def play(self):
#         print(f"{self.name} is playing.")

# # Derived class 2
# class Child2(Parent):
#     def __init__(self, name):
#         super().__init__(name)

#     def study(self):
#         print(f"{self.name} is studying.")

# # Create instances of Child1 and Child2
# child1 = Child1("Alice")
# child2 = Child2("Bob")

# child1.greet()  # From Parent
# child1.play()   # From Child1

# child2.greet()  # From Parent
# child2.study()  # From Child2

# -----------------------------------------------------------------

# Hybrid inheritance



