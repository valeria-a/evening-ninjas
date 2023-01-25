from lesson11.bank.customer import Customer


class Account:

    def __init__(self, account_id, branch_id, owners: list[Customer]):
        self.account_id = account_id
        self.branch_id = branch_id
        self.balance = 0
        self.owners = owners

    def withdraw(self, amnt) -> bool:
        if self.balance - amnt < 0:
            return False
        else:
            self.balance -= amnt
            return True