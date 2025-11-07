class Account:
    account_number : str
    balance : float
    account_owner_name : str
    
    def __init__(self, account_number: str, balance: float, account_owner_name: str) -> None:
        self.account_number = account_number
        self.balance = balance
        self.account_owner_name = account_owner_name
    
    def checkBalance(self) -> float:
        return self.balance
    
    def deposit(self, amount: float) -> str:
        self.balance += amount
        return "Deposit successful, new balance is " + str(self.balance)
    
    def withdraw(self, amount: float) -> str:
        if amount > self.balance:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return "Withdrawal successful, new balance is " + str(self.balance)
    
    def transfer(self, amount: float, to_account: 'Account') -> str:
        if amount > self.balance:
            return "Insufficient balance"
        else:
            self.balance -= amount
            to_account.balance += amount
            return "Transfer successful, new balance is " + str(self.balance)
    
def displayAccountDetails(account: Account) -> str:
    return f"Account Number: {account.account_number}, Account Owner: {account.account_owner_name}, Balance: {account.balance}"
    