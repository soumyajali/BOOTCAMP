actual_pin=9999
balance=5000
pin=int(input("Enter the pin: "))
if pin!=actual_pin:
    print("invalid pin")
elif pin==actual_pin:
    amount=int(input("Enter the amount: "))
    if(amount <= balance):
        balance -= amount
        print("Money debited sucessfully")
        print("Balance: ",balance)
    else:
        print("Insufficient balance")
else:
    print("enter valid pin")
