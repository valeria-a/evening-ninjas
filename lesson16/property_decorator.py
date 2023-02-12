# Using @property decorator
class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self._temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value...")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value


# create an object
human = Celsius(37)

print(human.temperature)

print(human.to_fahrenheit())

human.temperature = -300
# temp = human.temperature
# coldest_thing = Celsius(-300)


# In Python, property() is a built-in function that creates and
# returns a property object. The syntax of this function is:
#

# proprty(temperature)

# del human.temperature

# # make empty property
# temperature = property()
#
# # assign fget
# temperature = temperature.getter(get_temperature)
#
# # assign fset
# temperature = temperature.setter(set_temperature)