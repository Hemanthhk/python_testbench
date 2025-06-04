print("Object oriented programming - Mainly about grouping set of tasks in a method. And group set of methods related to a particular task/flow in a class")

# class Sample():
#     print("sample class")

# x = Sample()

# print(type(x),x)

# #Example 2:
# class Dog():

#     #CLASS OBJECT ATTRIBUTE - Global constant for a class
#     species = "mammal"

#     #__init__ method to initialize variables as soon as the object of the class is created.
#     def __init__(self,breed,name):
#         self.breed = breed
#         self.name = name
    

# my_dog = Dog(breed="Lab",name="Sweety")
# print(f"{my_dog.name} is a {my_dog.breed}")
# print(my_dog.species)

# # Example 3:

# class Circle():

#     pi = 3.14 #CLASS OBJECT ATTRIBUTE
#     def __init__(self,radius=1):
#         self.radius = radius

#     def area(self):
#         return self.radius*self.radius*Circle.pi
    
#     #Method to reset object attributes - Choice/Style of programming
#     def set_radius(self,new_r):
#         self.radius = new_r
    

# myc = Circle()
# myc.set_radius(3)
# print(myc.radius)
# print(myc.area())

#INHERITANCE - Creating new classes using older classes. 
# Created class is Derived class and the original is called base class.
# Reduces creating duplicate classes.

class Animal():

    def __init__(self):
        print("ANIMAL CREATED")

    def whoAmI(self):
        print("ANIMAL")
    
    def eat(self):
        print('EATING')


# mya = Animal()
# mya.whoAmI()
# mya.eat()

class Dog(Animal):  #Inherit Animal class

    def __init__(self):
        # Animal.__init__(self) #This is not mandatory
        print("DOG CREATED")
    
    #Can create additional methods not in base class
    def bark(self):     
        print("WOOF")
    
    #Can override the methods in the base class
    def eat(self):
        print("DOG EATING")
    

mydog= Dog()
mydog.whoAmI()
mydog.bark()
mydog.eat()  #Call overriden class

#SPECIAL METHODS - 
# __str___ - To return string representation instead of object to make it user friendly
#__len__ - To return when len is used from outside


class Book():

    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f"Title:{self.title}, Author: {self.author}, Pages: {self.pages}"
    
    def __len__(self):
        return self.pages
    
    def __del__(self):
        print("Deleted book object")


b = Book("Great Learning","hh",100)

print(b)  #Without special method, This would be an object  - <__main__.Book object at 0x0000028792888690>
print(len(b))

del b
