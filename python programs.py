[24bcs170@mepcolinux ex6]$cat combo2.py
from itertools import combinations
li = ['A','B','C','D']
print(list(combinations(li,2)))

[24bcs170@mepcolinux ex6]$cat combo2rep.py
from itertools import combinations_with_replacement
l = [1,2]
print(list(combinations_with_replacement(l,2)))

[24bcs170@mepcolinux ex6]$cat countuse.py
from itertools import count

counter = count(10)
for _ in range(5):
    print(next(counter), end=" ")
[24bcs170@mepcolinux ex6]$cat cycle3.py
from itertools import cycle

data = [5, 10, 15]
cycler = cycle(data)
for _ in range(len(data) * 3):
    print(next(cycler), end=" ")

[24bcs170@mepcolinux ex6]$cat list.py
from itertools import permutations
data = ['X','Y','Z']
print(list(permutations(data)))

[24bcs170@mepcolinux ex6]$cat per.py
from itertools import permutations
data = ['X','Y','Z']
print(list(permutations(data)))


[24bcs170@mepcolinux ex7]$cat bird.py
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Some sound")

class Bird(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def speak(self):
        print("Tweet")

my_bird = Bird("Parrot", "Green")
print(f"Name: {my_bird.name}")
print(f"Color: {my_bird.color}")
my_bird.speak()

[24bcs170@mepcolinux ex7]$cat car.py
class Car:
    def drive(self):
        print("Vroom!")

car1 = Car()
car2 = Car()

car1.drive()
car2.drive()

[24bcs170@mepcolinux ex7]$cat fan.py
class Fan:
    def __init__(self):
        self.speed = "Medium"

    def status(self):
        print("Fan speed:", self.speed)

fan = Fan()
fan.status()


[24bcs170@mepcolinux ex7]$cat rectangle.py
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rect = Rectangle(5, 3)

print(f"Area: {rect.area()}")