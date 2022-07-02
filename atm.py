class atm(object):
    def __init__(self, card, pin, amount, ):
        self.card = card
        self.pin = pin
        self.amount = amount
    
    def CashWithdrawl(self, card, pin, amount):
        self.pin[card]=pin
        self.amount[card]=amount
        print("You have withdrawn", amount)

    def BalanceEnquiry(self, card, pin):
        