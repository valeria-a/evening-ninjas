

# divide_dictionary_values(d, ['a'])

def divide_dictionary_values(dictionary, keys):
    try:
        key1 = keys[0]
        key2 = keys[1]
        print(dictionary[key1] / dictionary[key2])
    except (KeyError, IndexError) as error:
        print(f"Provided key or index does not exist: {error}")
    except ZeroDivisionError:
        print(f"You tried to divide by zero")
    except TypeError as val_err:
        print("TypeError", val_err)
    except Exception as unknown_exc:
        print(f"Unknown error of type {type(unknown_exc)}: {unknown_exc}")
    print('bye')


if __name__ == '__main__':
    d = {'a': 4, 'b': 0, 'c': 2, 'd': 'sdfsdf'}
    divide_dictionary_values(d, ['a', 'c'])
    divide_dictionary_values(d, ['a'])