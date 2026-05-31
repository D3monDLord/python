
card_insert = input("Card (yes/no) :")
if card_insert == "yes":
    
    pin_code = input("pin is correct? (yes/no)")
    if pin_code =="yes":
            balance = float(input("Enter your balance: "))
            withdraw = int(input("Enter the amount you want to withdraw: "))
            if balance > withdraw:
             if withdraw:
                 print("transaction sucessful")
             else:
                print("enter the number in the multiple of 100")
            else:
             print("insufficient balance")
    else:
     print("wrong pin")

else:
    print("insert card first")
    


