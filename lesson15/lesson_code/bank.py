import datetime


class Bank:

    def __init__(self, bank_name):
        self.name = bank_name

        # the following dictionary maps account number to password
        # that can be used to perform operations on the account
        self.passwords = {
            11111: "Pa$$w0rd!",
            22222: "$ecret123!"
        }

        # the following dictionary maps account numbers to account
        # balances (amount of money on the account)
        self.balances = {
            11111: 4500,
            22222: 2000
        }

    @staticmethod
    def working_hours_only(callable):

        print("Creating working_hours_only decorator")

        def wrapped_callable(*args, **kwargs):

            print("Checking working hours...")

            x = datetime.datetime.today()
            if x.strftime("%a") in ['Sun', 'Mon', 'Tue', 'Wed', 'Thu'] and \
                    22 > int(x.strftime("%H")) > 9:
                ret_val = callable(*args, **kwargs)
                return ret_val
            else:
                raise Exception("Outside working hours")

        return wrapped_callable


    @staticmethod
    def authenticate(callable):

        print("Creating authentication decorator")

        def wrapped_callable(*args, **kwargs):
            print("Authenticating...")
            bank = args[0]
            account_num = args[1]
            password = args[2]

            if account_num in bank.passwords and bank.passwords[account_num] == password:
                ret_val = callable(*args, **kwargs)
                return ret_val
            else:
                raise Exception("Could not authenticate")

        return wrapped_callable

    @staticmethod
    def validate_balance(callable):

        print("Creating validate_balance decorator")

        def wrapped_callable(*args, **kwargs):
            print("Validating balance...")
            bank = args[0]
            account_num = args[1]
            amount = args[3]

            print(f"You have ${bank.balances[account_num]} on your account")

            if bank.balances[account_num] >= amount:
                ret_val = callable(*args, **kwargs)
                return ret_val
            else:
                raise Exception("Not enough money")

        return wrapped_callable

    @working_hours_only
    @authenticate
    @validate_balance
    @classmethod
    def withdraw(self, account_num, password, amount):
        print(f"Called withdraw ${amount} for account {account_num}")

        self.balances[account_num] -= amount

        new_balance = self.balances[account_num]
        print(f"New balance for account {account_num} after withdraw is ${new_balance}")
        return new_balance
    # withdraw = working_hours_only(withdraw)
    # withdraw = working_hours_only(authenticate(validate_balance(withdraw)))



    def deposit(self, account_num, password, amount):
        print(f"Called deposit ${amount} for account {account_num}")

        self.balances[account_num] += amount

        new_balance = self.balances[account_num]
        print(f"New balance for account {account_num} after deposit is ${new_balance}")
        return new_balance


    def feedback(self, account_num, feedback):
        print("Your feedback is recorded")


if __name__ == '__main__':
    b = Bank('aaa')
    b.withdraw(11111, "Pa$$w0rd!", 450)