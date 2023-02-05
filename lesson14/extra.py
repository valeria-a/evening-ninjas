class Person:

    def __init__(self, passport_num, name, **kwargs):
        print(kwargs)
        self._passport_num = passport_num
        self._name = name
        for k, v in kwargs.items():
            self.__setattr__('_'+k, v)


if __name__ == '__main__':
    p = Person(123456789, 'Slava',
               address='Rehovot', phone='045729348')
    print('bye')
    p.__getattribute__('_address')
