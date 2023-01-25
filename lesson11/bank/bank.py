from lesson11.bank.account import Account
from lesson11.bank.branch import Branch
from lesson11.bank.customer import Customer


class Bank:

    def __init__(self, name, hq_address):
        self.name = name
        self.hq_address = hq_address

        self.branches_by_id: dict[int, Branch] = {}
        self.branches_by_city: dict[str, list[Branch]] = {}

        self.accounts_by_id: dict[int, Account] = {}

        self.customers_by_id: dict[int, Customer] = {}

    def add_branch(self, branch_id, name, address, city) -> bool:
        branch = Branch(branch_id, name, address, city)
        self.branches_by_id[branch_id] = branch
        self.branches_by_city[city] = branch
        return True

    def update_branch_address(self, branch_id, new_address) -> bool:
        branch = self.branches_by_id.get(branch_id)
        if not branch:
            return False
        branch.set_address(new_address)

    def add_account(self, account_id, branch_id, owner_ids):
        customers = []
        for o_id in owner_ids:
            if o_id not in self.customers_by_id:
                return False
            customers.append(self.customers_by_id[o_id])

        account = Account(account_id, branch_id, customers)
        self.accounts_by_id[account_id] = account

    def withdraw(self, account_id, amnt):
        if account_id in self.accounts_by_id:
            return self.accounts_by_id[account_id].withdraw(amnt)
        else:
            return False

