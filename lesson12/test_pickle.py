import pickle
from files6 import Table

if __name__ == '__main__':
    with open('table.pickle', 'rb') as f:
        my_table = pickle.load(f)
    print(my_table)