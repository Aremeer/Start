class Student:
    def __init__(self, name, house):
        self.house = house
        self.name = name

    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing Name")
        self._name = name

    @property
    def house(self):
        return self._house
    @house.setter 
    def house(self, house):
        if house not in ["Gryffindor","Hufflepuff","Ravenclaw","Slytherin"]:
            raise ValueError("invalid house")
        self._house = house


def main():
    print(get_student())

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house,)





if __name__ == "__main__":
    main() 