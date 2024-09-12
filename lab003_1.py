class BankAccount:
    bank_name = "DNB"
    interest_rate = 0
    all_account=[]
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.balance = balance
    
    #Method deposite with instance variable balance 
    def balance()