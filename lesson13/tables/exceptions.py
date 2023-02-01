class TableSystemError(Exception):
    pass


class TableAlreadyReserved(TableSystemError):
    pass


class TooManyGuests(TableSystemError):
    pass


class TableAlreadyAvailable(TableSystemError):
    pass