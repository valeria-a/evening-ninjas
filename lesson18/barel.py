from threading import Lock
from concurrent.futures import ThreadPoolExecutor


class BankAccount:

    def __init__(self):

        self._balance = 0
        self._transactions = []
        self._lock_balance = Lock()
        self._lock_transaction = Lock()

    def deposit(self, money_to_add):
        with self._lock_balance:
            with self._lock_transaction:
                self._balance += money_to_add
                self._transactions.append({'type': 'deposit', 'amount': money_to_add})

    def withdraw(self, money_to_withdraw):
        with self._lock_balance:
            with self._lock_transaction:
                self._balance -= money_to_withdraw
                self._transactions.append({'type': 'withdraw', 'amount': money_to_withdraw})

    def get_balance(self):
        with self._lock_balance:
            return self.get_balance()


if __name__ == '__main__':
    account = BankAccount()

    def multiple_transactions_deposit(account):
        for i in range(100, 2000000, 10):
            account.deposit(i)


    def multiple_transactions_withdraw(account):
        for i in range(100, 2000000, 10):
            account.withdraw(i)


    with ThreadPoolExecutor(4) as executor:
        executor.submit(multiple_transactions_deposit, account)
        executor.submit(multiple_transactions_withdraw, account)

    assert account._balance == 0, \
        f"Expected balance: 0, received: {account._balance}"
    assert len(account._transactions) == 399980, \
        f"Expected transactions: 399980, received: {len(account._transactions)}"