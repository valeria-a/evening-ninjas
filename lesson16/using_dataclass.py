from dataclasses import dataclass, field


# class Company:
#     def __init__(self, name, address, employees_number):
#         self.name = name
#         self.address = address
#         self.employees_number = employees_number

# c1 = Company('McDonalds', 'ccc', 50000)
# c3 = Company('McDonalds', 'ccc', 50000)
# c1 == c3
# c2 = Company('Apple', 'bbb', 10000),
# sorted([c1, c2])


@dataclass(frozen=False, order=True)
class Company:
    name: str
    address: str
    employees_number: int = 50 # default value


c = Company('Apple', 'California', 10000)
print(c)
#
c2 = Company('Apple', 'California', 10000)
#
print(c == c2)
c.name = 'bla'
companies = [Company('McDonalds', 'ccc', 50000), Company('Apple', 'bbb', 10000), ]
print(sorted(companies))



@dataclass(order=True)
class Company:
    sort_index: int = field(init=False, repr=False)
    name: str
    address: str
    employees_number: int = 50 # default value




    def is_big_company(self):
        return self.employees_number > 10000

    def __post_init__(self):
            self.sort_index = -self.employees_number

@dataclass
class FoodCompany(Company):
    food_type: str = 'various'

companies = [Company('McDonalds', 'ccc', 50000), Company('Apple', 'bbb', 10000), ]

print(sorted(companies))


# @dataclass(frozen=True)
# class Company():
#     name: str
#     address: str
#     employees_number: int = 50 # default value
#
#
# c = Company('McDonalds', 'ccc', 50000)
# c.employees_number = 5


