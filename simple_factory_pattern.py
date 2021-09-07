
from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):

    @abstractmethod
    def do_say(self):
        pass


class Cat(Animal):

    @classmethod
    def do_say(cls):
        print("mio mio")


class Dog(Animal):

    @classmethod
    def do_say(cls):
        print("hap hap")


class ForestFactory:

    def makesound(self, object_type):
        return eval(object_type).do_say()


if __name__ == '__main__':

    ff = ForestFactory()
    animal = input("please enter the animal name : ")
    ff.makesound(animal)

