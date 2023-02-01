import os
import pickle


class BestBusCompany:

    def __init__(self):
        self._routes = []


if __name__ == '__main__':

    # check whether this is the first time you run the app
    # if this is the first time - create a new class
    if not os.path.exists('bus_company.pickle'):
        bus_company = BestBusCompany()
    else:
        # this is not the first time - we already have a DB
        # with data from the previous runs
        with open('bus_company.pickle', 'rb') as fh:
            bus_company = pickle.load(fh)

    try:
        pass
    #
    # here comes your code that runs main menu
    # and interacts with the user and adds/ updates
    # data in your bus_company class
    except Exception as e:
        print("Error occurred, exiting...", e)

    finally:
        print("This code will be executed both if exception occurred or not")
        # before exiting the program, persist the current state
        # of te system in the file, so next time it will be loaded

        with open('bus_company.pickle', 'wb') as fh:
            pickle.dump(bus_company, fh)
