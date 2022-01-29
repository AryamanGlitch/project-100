class Atm(object):
    def __init__(self,amount,pin,expiryDate):
        self.amount = amount
        self.pin = pin
        self.expiryDate = expiryDate
       
    def cashWithdrawl(self):
        print("Cash Withdrawl")
    def balanceEnquiry(self):
        print("Balance Enquiry")
    def AmountDebitted(self):
        print("Amount Debitted")
    def IncorrectPin(self):
        print("Incorrect Pin")    

atm = Atm("$100","1234","22/08/22")   

print (atm.IncorrectPin())