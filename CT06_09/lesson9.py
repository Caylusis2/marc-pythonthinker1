# print("Hello from lesson 9")

# import random

# num1= random.randint(1, 6)
# num2= random.randint(1, 6)
# num3= random.randint(1, 6)

# print("1st number is: " + str(num1))
# print("2nd number is: " + str(num2))
# print("3rd number is: " + str(num3))

# num1_isEven= num1 % 2 == 0
# num2_isEven= num1 % 2 == 0
# num3_isEven= num3 % 2 == 0

# all_even_add = num1_isEven == num2_isEven

# print(all_even_add)

# numberofdays=int(input("How many days have your book been borrowed?"))

# if numberofdays > 25:
#     print("Remember to return your book!")

# import random

# num= random.randint(1, 10)

# userguess=int(input("Guess the number: "))

# if userguess == num:
#     print("Congratulations!")

# price_apple = 0.60
# price_orange = 0.90

# num_apples=input("How many apples do you wan tot buy?")
# num_oranges=input("How many oranges do you want to buy?")

# if num_apples > 5:
#     costApple = num_apples * price_apple * 0.9

# if num_apples < 5:
#     costApple = num_apples * price_apple

# if num_oranges > 5:
#     costOrange = num_oranges * price_orange * 0.9

# if num_oranges > 5:
#     costOrange = num_oranges * price_orange

# total =costOrange + costApple

# print(total)

positive_days=0

for i in range(7):
    temp = int(input("What is the temperature for today?"))
    if temp > 30:
        positive_days += 1 
print(positive_days)

desirable=0
undesirable=0

for i in range(10):
    ratings=int(input("How is the hotel experience?"))
    if ratings > 3:
        desirable +=1
    if ratings <= 3:
        undesirable += 1

print()









