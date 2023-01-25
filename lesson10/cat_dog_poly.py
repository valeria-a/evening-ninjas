class Cat:
    def __init__(self, cat_type, color, name):
        self.cat_type = cat_type
        self.color = color
        self.name = name

    def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self, dog_type, color, name):
        self.dog_type = dog_type
        self.color = color
        self.name = name

    def make_sound(self):
        print("Wof")


cat = Cat('russian blue', 'grey-blue', 'Oliver')
cat2 = Cat('persian', 'white', 'Mitzi')
dog = Dog('doberman', 'black', 'Bruno')
dog2 = Dog('bulldog', 'white-and-brown', 'Max')
dog3 = Dog('chihuahua', 'red', 'Daisy')

#
# cat.make_sound()
# dog.make_sound()

# print(cat.name, dog.name)

# animals_list = [cat, dog, dog2, cat2, dog3]
# for animal in animals_list:
#     # print(animal.name)
#     animal.make_sound()


l1 = [1,2,3]
l2 = [4,5,6]
print(l1 + l2)

n1 = 4
n2 = 7
print(n1 + n2)

w1 = "Hello "
w2 = "World"
print(w1 + w2)










