from typing import AsyncContextManager, AwaitableGenerator


class Dog:
    #class atttribute
    species = "mammal"

    #Initialize / instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
    #instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    def bark_at(self, other_dog):
        print(f"{self.name} barked furiously at {other_dog.name}")


nelson = Dog('Nelson', 3)
baxter = Dog('Baxter', 16)


print(nelson.description)
print(baxter.description)

nelson.bark_at(baxter)