import sys
import argparse

if __name__ == '__main__':
    # name - positional
    # age - positional
    # address - named
    # phone - named

    # python my_script.py valeria 36 --phone 45837456
    # python my_script.py --phone 45837456 valeria 36
    # python my_script.py --phone 45837456 valeria aaa

    parser = argparse.ArgumentParser()

    parser.add_argument('name', help="The name of the person")
    parser.add_argument('age', type=int)
    parser.add_argument('--address', '-a')
    parser.add_argument('--phone')

    parsed_arguments = parser.parse_args()

    print(f"Name: {parsed_arguments.name},"
          f"Age: {parsed_arguments.age},"
          f"Address: {parsed_arguments.address},"
          f"Phone: {parsed_arguments.phone}")
    # parsed_arguments.name
    # parsed_arguments.age


