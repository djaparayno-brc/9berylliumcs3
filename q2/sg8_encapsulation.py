class BankAccount:
    def __init__(self, account_number: int = 0, balance: float = 0.0):
        self.__account_number = None
        self.__balance = 0.0
        self.set_account_number(account_number)
        self.set_balance(balance)

    def get_account_number(self) -> int:
        return self.__account_number

    def set_account_number(self, account_number: int):
        if isinstance(account_number, int) and account_number > 0:
            self.__account_number = account_number
        else:
            print("Account number must be a positive integer. Try again, it must not be negative this time.")

    def get_balance(self) -> float:
        return self.__balance

    def set_balance(self, balance: float):
        if balance >= 0.0:
            self.__balance = float(balance)
        else:
            print("The balance must not be a negative number.")

if __name__ == "__main__":
    print("Output:")
    print("Account 1")
    accounta1 = BankAccount(676767, 676.67)
    print(f"Account Number: {accounta1.get_account_number()}")
    print(f"Balance: {accounta1.get_balance()}")
    print()
    print(f"Update balance to -150.00")
    accounta1.set_balance(-150.00)
    print(f"Account Number: {accounta1.get_account_number()}")
    print(f"Before Balance: {accounta1.get_balance()}")
    accounta1.set_balance(750.25)
    print(f"After Balance: {accounta1.get_balance()}")

