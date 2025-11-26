balance = 5000

pin = 1234

userpin= int(input("Enter your PIN: "))
 
count=1
max=3
while(count<max):
    userpin= int(input("Enter your PIN: "))

    if userpin== pin:

        amount=int(input("Enter amount to withdraw: "))

        if amount <= balance:

            balance-=amount
            print("Withdrawal successful")

            print("Remaining Balance:", balance)




        else:



            print("Insufficient Balance")
    elif userpin!=pin:
        count+=1
    elif count==max:
        break
