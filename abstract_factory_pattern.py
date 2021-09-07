
from abc import ABCMeta, abstractmethod


class PizzaFactory(metaclass=ABCMeta):

    @abstractmethod
    def createVegpizza(self):
        pass

    @abstractmethod
    def createNoneVegpizza(self):
        pass


class Vegpizza(metaclass=ABCMeta):

    @abstractmethod
    def prepare(self):
        pass


class NonVegpizza(metaclass=ABCMeta):

    @abstractmethod
    def serve(self, Nonvegpizza):
        pass


class DeluxVegPizza(Vegpizza):

    def prepare(self):
        print(type(self).__name__, "prepare")


class ChickenPizza(NonVegpizza):

    def serve(self, Nonvegpizza):
        print(type(self).__name__, "served", type(Nonvegpizza).__name__)


class MexicanVegPizza(Vegpizza):

    def prepare(self):
        print(type(self).__name__, "prepare")


class HamPizza(NonVegpizza):
    def serve(self, Nonvegpizza):
        print(type(self).__name__, "served", type(Nonvegpizza).__name__)


class IndianPizzaFactory(PizzaFactory):

    def createVegpizza(self):
        return DeluxVegPizza()

    def createNoneVegpizza(self):
        return ChickenPizza()


class UsPizza(PizzaFactory):

    def createVegpizza(self):
        return MexicanVegPizza()

    def createNoneVegpizza(self):
        return HamPizza()


class PizzaStore:

    def __init__(self):
        pass


    def makePizzas(self):
        for factory in [IndianPizzaFactory(), UsPizza()]:
            self.factory = factory
            self.NonVegPizza = self.factory.createNoneVegpizza()
            self.VegPizza = self.factory.createVegpizza()
            self.VegPizza.prepare()
            self.NonVegPizza.serve(self.VegPizza)


pizza = PizzaStore()
pizza.makePizzas()