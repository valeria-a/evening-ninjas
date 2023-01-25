import datetime


class Person:

    def __init__(self, first_name: str, last_name: str, address: str,
                 email: str, bdate: datetime.date):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__address = address
        self.__email = email
        self._birth_date: datetime.date = bdate

    def get_full_name(self):
        return f"{self.__first_name} {self.__last_name}"

    def get_address(self):
        return self.__address

    def get_email(self):
        return self.__email

    def get_birth_date(self) -> datetime.date:
        return self._birth_date

    def get_age(self):
        return datetime.date.today().year - self._birth_date.year


    def __str__(self):
        return f"{self.get_full_name()}, " \
               f"lives at {self.get_address()}, " \
               f"{self.get_age()} years old"

    def __repr__(self):
        return self.__str__()


# override
# overwrite

class Student(Person):

    def __init__(self, first_name: str, last_name: str,
                 address: str, email: str, bdate: datetime.date, study_year):
        super().__init__(first_name, last_name, address, email, bdate)
        self.study_year = study_year
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def _get_grades_sum(self):
        return sum(self.grades)

    def get_avg_grade(self):
        return self._get_grades_sum() / len(self.grades)

    def get_full_name(self):
        return self._Person__first_name

    def print_hello(self):
        print(self._birth_date)
        # calls 2 different methods
        print(self.get_full_name())
        print(super().get_full_name())

        # calls the same method (from Person class)
        print(self.get_age())
        print(super().get_age())

    def __str__(self):
        return f"Student: {super().__str__()}"


class Lecturer(Person):

    def __init__(self, first_name: str, last_name: str, address: str, email: str, bdate: datetime.date, salary: int):
        super().__init__(first_name, last_name, address, email, bdate)
        self.salary = salary

    def get_course_payment(self, hours_amnt:int):
        return self.salary * hours_amnt


class LeadLecturer(Lecturer):

    def __init__(self, first_name: str, last_name: str, address: str, email: str, bdate: datetime.date, salary: int):
        super().__init__(first_name, last_name, address, email, bdate, salary)
        self.conferences = []

    def add_conference(self, conf_name):
        self.conferences.append(conf_name)

    def get_course_payment(self, hours_amnt:int):
        return super().get_course_payment(hours_amnt) + 3000



if __name__ == '__main__':
    # s = Student("David", "Shwimmer", "US", "david@gmail.com", datetime.date(1965, 11,2), 2023)
    # print(s)
    # print(s.get_age())
    #
    # print(isinstance(s, Student))
    # print(isinstance(s, Person))
    #
    # p = Person("David", "Koperfield", "US", "davidk@gmail.com", datetime.date(1963, 11, 2))
    # print(p.get_age())
    # print(s.get_age())
    #
    # s.print_hello()
    # p.print_hello()

    # s1 = Student()
    # print(s1)

    # s.add_grade(90)
    # s.add_grade(99)
    # print(s.get_avg_grade())

    # s.print_hello()

    # print(p)
    # print(s)

    l1 = LeadLecturer('aaa','bbb','ccc','ddd',None, 100)
    payment = l1.get_course_payment(30)
    print(l1._birth_date)