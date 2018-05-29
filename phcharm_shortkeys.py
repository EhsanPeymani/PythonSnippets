class Pet(object):
    def __init__(self, name, age): # alt + enter for adding field to class
        self.__age = age # fully private field
        self.name = name

    # do not create new fields outside of __init__ as it becomes very hard to follow

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        self.__age = new_age


if __name__ == '__main__': # write main and press tab for this autocomplete
    cow = Pet('AA', 10)
    print(cow.age)

    cow.age = 20
    print(cow.age)



