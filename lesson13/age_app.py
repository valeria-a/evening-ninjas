import datetime


class FutureBirthDateException(Exception):

    def __init__(self, birth_date):
        # super().__init__(msg)
        self.birth_date = birth_date

    def __str__(self):
        return f"FutureBirthDateException: {self.birth_date}"


def get_age(birth_date: datetime.date):
    if birth_date > datetime.date.today():
        # raise Exception("future birth date")
        raise FutureBirthDateException(birth_date)
    return datetime.date.today().year - birth_date.year


if __name__ == '__main__':
    while True:
        bdate = input("Insert your birth date in format dd-mm-yy: ")
        try:
            bdate = datetime.datetime.strptime(bdate, '%d-%m-%y')
            age = get_age(bdate.date())
            print(f"You are {age} years old")
        except ValueError as e:
            print("You inserted a date in a wrong format, try again")
        except FutureBirthDateException as e:
            # e.birth_date
            print(e)
        except Exception as e:
            print("Unexpected error: ", e)
            break

# if __name__ == '__main__':
#     print(type(FutureBirthDateException))
#     print(type(FutureBirthDateException()))