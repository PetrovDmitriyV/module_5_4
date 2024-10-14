# class Example:
#     def __new__(cls, *args, **kwargs):
#         print(args)
#         print(kwargs)
#         return object.__new__(cls)
#
#     def __init__(self, first, second, third):
#         print(first)
#         print(second)
#         print(third)
#
#
# ex = Example('data', second=25, third=3.14)


class House:
    houses_history = []

    def __new__(cls, *args):
        names = list(args)
        for key in names:
            if isinstance(key, int):
                continue
            else:
                names = [key]
                cls.houses_history = cls.houses_history + names
        return object.__new__(cls)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        return print(f'{self.name} снесён, но он останется в истории')


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3
print(House.houses_history)
