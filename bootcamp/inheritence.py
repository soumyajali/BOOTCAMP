class Animal:
    def sound(self):
        print("Animal makes sound")

class Pet:
    def play(self):
        print("Pet loves playing")

class Dog(Animal, Pet):
    def bark(self):
        print("Dog barks")

d = Dog()

d.sound()
d.play()
d.bark()
