class Cats:
    name = None
    age = None
    isHappy = None

    def __init__(self, name, age, isHappy = None):
        # self.name = name
        # self.age = age
        # self.isHappy = isHappy
        self.set_data(name, age, isHappy)
        self.get_data()

    # def __init__(self):
    #     pass

    def set_data(self, name, age, isHappy = None):
        self.name = name
        self.age = age
        self.isHappy = isHappy

    def get_data(self):
        print(self.name, self.age, self.isHappy)


# cat1 = Cats()
# cat1.name = 'Barsik'
# cat1.age = 3
# cat1.isHappy = True

cat1 = Cats("Barsik", 3, True)
cat1.set_data("sdd", 1)

# cat2 = Cats()
# cat2.set_data("Murzik", 4, False)

# print(cat1.name)
# print(cat2.name)

# cat2.get_data()
# cat1.get_data()
