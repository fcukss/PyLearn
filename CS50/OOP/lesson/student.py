import sys


class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f'Student - {self.name} from {self.house}'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            sys.exit('Missing name')
        self._name = name

    # getter
    @property
    def house(self):
        """

        :return:
        """
        return self._house

    @house.setter
    def house(self, house):
        if house not in ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']:
            raise ValueError('Invalid house')
        self._house = house

    @classmethod
    def get(cls):
        name = input("Name ")
        house  = input('House ')
        return cls(name, house)


def main():
    print(Student.get())


if __name__ == '__main__':
    main()
