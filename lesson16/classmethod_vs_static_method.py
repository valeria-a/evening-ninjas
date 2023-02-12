class BEstFruit:

    # tropical =
    green = ('apple', 'pear')

    def __init__(self, name, color):
        self._name = name
        self._color = color

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    @staticmethod
    def get_tropical_fruit():
        return ('ananas', 'passionfruit')

    @classmethod
    def get_green_fruits(cls):
        return cls.green


if __name__ == '__main__':
    # Fruit.get_tropical_fruit()
    # Fruit.get_green_fruits()
    pass