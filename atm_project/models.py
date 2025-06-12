# temporary database
class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

accounts = [
    Account('111', 1000),
    Account('222', 500),
]

# return acoount by number account
def get_account_by_number(account_number):
    for acc in accounts:
        if acc.account_number == account_number:
            return acc
    return None
