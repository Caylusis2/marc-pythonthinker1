# print("Hello from lesson 13")

# account_balance = 1000
# while True:
#     print("Choose between the four options below using the options number...")
#     print("1. Withdraw")
#     print("2. Deposit")
#     print("3. Check balance")
#     print("4. Exit")

#     userChoice=int(input("Your choice: "))

#     if userChoice == 1:
#         amount=int(input("How much do you want to withdraw? "))

#         if amount <= account_balance:
#             account_balance -= amount
#             print("You have successfully withdrew the amount. ")
#             print("The current balance is: $" + str(account_balance))
#         else:
#             print("Error: Declined. Not enough money!")

#     if userChoice == 2:
#         amount= int(input("How much do you want to deposit?:")) 
#         balance += amount
        
#     if userChoice == 3:
#         print("You currently have $" +)

#     if userChoice == 4:
#         break

groceries = [
    "Apples",
    "Bread",
    "Carrots",
    "Dates",
    "Eggs",
    "Flour",
    "Grapes",
    "Honey"
]

groceries[7] = "Herbs"

print(groceries)

groceries.append("Ice")
groceries.insert(1, "bananas")

print(groceries)

del(groceries[2])

print(groceries)



        
        

# this is the syntax:
# groceries = [
#     "Apples",
#     "Oranges"
# ]