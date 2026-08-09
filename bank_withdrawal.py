name = input ("enter your  name")
age =  int (input("enter your age"))
job =  input ("enter you job")
gender = input ("enter your gender")

the balance = float(input("enter your balance"))
withdraw amount = float(input ("enter the amount you want to withdraw"))
minimum balance = float(input("enter your minimum"))


print ("your is" + name + "and your age is" + str(age) + "years old" + "you work as" + job + "you are a " + gender  )


   def check_withdrawal( balance , withdraw_amount , minimum_balance )

    if balance >= withdraw amount  and (balance - withdraw_amount) >= minimum_balance
        
           print("you can withdraw this amount")

    elif  minimum balance > withdraw amount
        
           print("you can't withdraw this amount").

     
check_withdrawal(balance, withdraw_amount, minimum_balance)

