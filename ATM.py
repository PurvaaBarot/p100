class ATM :
    def __init__(self , cardnumber , pin):
        self.cardnumber=cardnumber
        self.pin=pin

    def balanceInquire (self):
        print("Your Balance is $1000000")

    def cashwidthdrawal(self,amountleft):
        new_amount = 1000000-amountleft
        print("Your withdrawl : " +str(amountleft)+ "Your balance is :"+ str(new_amount))
        
def function():
    name=input("Enter your name here: ")
    print("hello "+ name)
    cardnumber=input("Enter your cardnumber: ")
    pin=input("Enter the pin here: ")
    user = ATM(cardnumber,pin)

    print("Choose the method you want to go with")
    print("1. Balance Enquirey")    
    print("2. Cash Withdrawal")
    method=int(input("Enter your method [Either 1 or 2]: "))

    if(method== 1):
        user.balanceInquire()
    elif(method== 2):
        amountleft=int(input("Enter the amount to withdraw"))
        user.cashwidthdrawal(amountleft)
    else:
        print("Enter a valid number")

function()            








