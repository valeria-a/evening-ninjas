import datetime
import os.path
import pickle

from lesson13.tables.exceptions import *


class Table:

    def __init__(self, table_id, seats, max_time_limit=datetime.timedelta(minutes=90)):
        self.table_id = table_id
        self.seats = seats
        self.occupied_seats = 0
        self.start_time = None
        self.location = None
        self.max_time_limit = max_time_limit

    def is_available(self):
        return self.occupied_seats == 0

    def reserve(self, guests_num):

        # we allow to reserve a table only if it's available
        # and amount fo guests fits the amount of seats
        if self.occupied_seats != 0:
            raise TableAlreadyReserved()
        if self.seats < guests_num:
            raise TooManyGuests()

        self.occupied_seats = guests_num
        self.start_time = datetime.datetime.utcnow()

    def release(self):

        # The table is already available
        if self.occupied_seats == 0:
            raise TableAlreadyAvailable()

        self.occupied_seats = 0
        self.start_time = None

    def _get_end_time(self):
        return self.start_time + self.max_time_limit

    def time_left(self) -> datetime.timedelta:

        if not self.start_time:
            return datetime.timedelta()
        return self._get_end_time() - datetime.datetime.utcnow()

    def get_available_time(self) -> datetime.datetime:

        if not self.start_time:
            return datetime.datetime.utcnow()

        return self.start_time + self.max_time_limit

    def __str__(self):
        return f"Table id {self.table_id}, seats: {self.seats}, available: {self.is_available()}"

    def __repr__(self):
        return f"Table {self.table_id} ({self.seats})"


if __name__ == '__main__':
    t = Table(1, 3)
    t.reserve(2)
    try:
        t.reserve(2)
        try:
            num = int(input("insert a num:"))
        except:
            print('error')
    except TableSystemError as e:
        print("Error occurred")
        try:
            num = int(input("insert another num:"))
        except:
            print('error2')
    print("bye")


