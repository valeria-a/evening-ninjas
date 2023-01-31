import datetime


def get_age(birth_date: datetime.date):
    return datetime.date.today().year - birth_date.year


if __name__ == '__main__':
    bdate = input("Insert your birth date in format dd-mm-yy: ")
    bdate = datetime.datetime.strptime(bdate, '%d-%m-%y')
    age = get_age(bdate)
    print(f"You are {age} years old")