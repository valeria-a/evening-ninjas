from lesson11.bank.account import Account


class Customer:

    def __init__(self, customer_id, name, address, bdate, credit_score):
        self.customer_id = customer_id
        self.name = name
        self.address = address
        self.bdate = bdate
        self.credit_score = credit_score