from threading import Lock


class Car:

    def __init__(self, manufacturer: str, model: str, color: str,
                 tank_capacity: float, fuel_consumption: float):

        self._lock = Lock()
        self._color_lock = Lock()

        self.__colors_list = [color]
        self.__model = model
        self.__manufacturer = manufacturer
        self.__fuel_consumption = fuel_consumption
        self.__tank_capacity = tank_capacity

        self.__km = 0
        self.__fuel = 0


    def get_color(self):
        with self._color_lock:
            return self.__colors_list[-1]

    def set_color(self, new_color: str) -> bool:
        if new_color == 'silver':
            return False
        with self._color_lock:
            self.__colors_list.append(new_color)
        return True


    def add_fuel(self, fuel_to_add: float) -> bool:
        """
        Adds fuel to a car
        :param fuel_to_add:
        :return: True if succeeded, False otherwise
        """
        if fuel_to_add < 0:
            return False
        with self._lock:
            new_fuel = self.__fuel + fuel_to_add
            if new_fuel > self.__tank_capacity:
                return False
            else:
                self.__fuel = new_fuel
                return True

    def drive(self, km: float) -> bool:
        if km < 0:
            return False
        with self._lock:
            available_range = self.__fuel * self.__fuel_consumption
            if available_range < km:
                return False
            self.__km += km
            self.__fuel -= km / self.__fuel_consumption
            return True

    def __str__(self):
        with self._lock:
            with self._color_lock:
                return f"<Car\nmanufacturer:{self.__manufacturer}\nmodel: {self.__model}\n" \
               f"km: {self.__km}\nfuel: {self.__fuel}>, color:{self.get_color()}"


    def __repr__(self):
        return f"<Car> {self.__manufacturer} {self.__model}"