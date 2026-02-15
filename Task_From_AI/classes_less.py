class Human:
    __name: str
    __location: str

    def __init__(self, name = 'Ivan'):
        self.__name = name
        self.__location = 'London'

    def get_location(self):
        return self.__location

    def set_location(self, location):
        self.__location = location

class Child(Human):
    __age = 5
    def __init__(self, name = 'Tom'):
        super().__init__(name)
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__name +" : "+str(self.__age)

    def get_name(self):
        return self.__name

    def __repr__(self):
        return f'{self.get_name()} : {self.get_location()}'

class Bus:
    __child_sits : list()

    def __init__(self, child_sits):
        self.__child_sits = child_sits

    def add_children(self, child_sits):
        self.__child_sits = self.__child_sits + child_sits

    def remove_child(self, children : list):
        for child in children:
            if child in self.__child_sits:
                self.__child_sits.remove(child)

    def print_all_children(self):
        for child in self.__child_sits:
            print(child)

    def go_to_new_location(self, new_location):
        for child in self.__child_sits:
            child.set_location(new_location)

human = Human()
print(human.get_location())

child1 = Child()
print(child1.get_location())
print(child1.get_age())
print("_"*20)


child2 = Child(name = 'Harry')
child3 = Child(name = 'Ron')

bus = Bus([child1])
bus.print_all_children()
print("__"*10)
bus.add_children([child2])
bus.add_children([child3])
bus.print_all_children()
print("__"*10)
bus.remove_child([child2])
bus.print_all_children()
print("__"*10)
bus.go_to_new_location('Berlin')
bus.print_all_children()