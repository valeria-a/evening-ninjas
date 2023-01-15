car = {
    'manufacturer': 'mazda',
    'model': '3',
    'color': 'white',
    'fuel_capacity': 60,
    'fuel_consumption': 12,
    'km': 100000,
    'fuel': 30
}

# car['km'] = car['km']-100
#
# def drive_car(my_car, km):
#     pass
#
#
# def add_fuel(my_car, liters):
#     pass


class Car:

    def __init__(self, manufacturer: str, model: str, color: str,
                 tank_capacity: float, fuel_consumption: float):
        print("inside __init__ of Car")
        self.color = color
        self.model = model
        self.manufacturer = manufacturer
        self.fuel_consumption = fuel_consumption
        self.tank_capacity = tank_capacity

        self.km = 0
        self.fuel = 0

    def add_fuel(self, fuel_to_add: float) -> bool:
        """
        Adds fuel to a car
        :param fuel_to_add:
        :return: True if succeeded, False otherwise
        """
        print("inside add_fuel")
        new_fuel = self.fuel + fuel_to_add
        if fuel_to_add < 0 or new_fuel > self.tank_capacity:
            return False
        else:
            self.fuel = new_fuel
            return True

    def drive(self, km: float) -> bool:
        if km < 0:
            return False
        available_range = self.fuel * self.fuel_consumption
        if available_range < km:
            return False
        self.km += km
        self.fuel -= km / self.fuel_consumption
        return True

    def __str__(self):
        return f"<Car\nmanufacturer:{self.manufacturer}\nmodel: {self.model}\nkm: {self.km}\nfuel: {self.fuel}>"


    def __repr__(self):
        return f"<Car> {self.manufacturer} {self.model}"


if __name__ == '__main__':
    car_mazda = Car("Mazda", "3", "white", 60, 12)
    print(car_mazda.tank_capacity)

    car_toyota = Car("Toyota", "Yaris", "red", 40, 15)

    print(car_mazda.manufacturer)
    print(car_toyota.manufacturer)

    print(isinstance(car_mazda, Car))
    print(isinstance(car_mazda, str))

    print(type(car_mazda) == Car)
    print(type(car_mazda))

    car_toyota.color = 'blue'
    print(car_toyota.color)
    ret_val = car_toyota.add_fuel(20)
    if ret_val:
        print("Succeeded")
    else:
        print("Failed to add fuel - tank is full")
    print(f"km before: {car_toyota.km}, fuel before: {car_toyota.fuel}")
    print(car_toyota.drive(100))
    print(f"km after: {car_toyota.km}, fuel after: {car_toyota.fuel}")

    print(car_toyota)

    cars_list = [car_mazda, car_toyota]
    print(cars_list)


    # car_toyota.fuel += 20
    # car_toyota.manufacturer = 'honda'

    # car_mazda.add_fuel()
    # Car.add_fuel(car_mazda)

    # l = [2,4,5]
    # l.count(2)
    # list.count(l, 2)

    # print(type(car))
    # print(type(Car))
    # print(type(WaterApp))
    # print(type(str))
class WaterApp:
    pass




