from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    @abstractmethod
    def create_chair(self):
        raise NotImplementedError()

    @abstractmethod
    def create_sofa(self):
        raise NotImplementedError()

    @abstractmethod
    def create_table(self):
        raise NotImplementedError()


class Chair:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Sofa:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Table:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class AbstractFurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self):
        pass

    @abstractmethod
    def create_table(self):
        pass

    @abstractmethod
    def create_sofa(self):
        pass


class VictorianFactory(AbstractFurnitureFactory):
    def create_chair(self):
        return Chair("Victorian chair")

    def create_table(self):
        return Table("Victorian table")

    def create_sofa(self):
        return Sofa("Victorian sofa")


class FuturisticFactory(AbstractFurnitureFactory):
    def create_chair(self):
        return Chair("Futuristic chair")

    def create_table(self):
        return Table("Futuristic table")

    def create_sofa(self):
        return Sofa("Futuristic sofa")


class ModernFactory(AbstractFurnitureFactory):
    def create_chair(self):
        return Chair("Modern chair")

    def create_table(self):
        return Table("Modern table")

    def create_sofa(self):
        return Sofa("Modern sofa")


def get_furniture(style):
    if style == "Victorian":
        factory = VictorianFactory()
    elif style == "Futuristic":
        factory = FuturisticFactory()
    # elif style == "Modern":
    else:
        factory = ModernFactory()

    return factory.create_sofa(), factory.create_chair(), factory.create_table()


request = input()   # Modern, Victorian, Futuristic

print(get_furniture(request))
