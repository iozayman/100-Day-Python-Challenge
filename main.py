#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇


Bill = input("What was the total bill?\n$")
Tip = input("How much tip would you like to give?\n{Example 10, 12 or 15 DONT BE SELFISH we can calculate more}\n%")
People = input("How many people to split the bill?\n")

Result = round((float(Bill) / int(People)) * float(int(Tip) / 100 + 1), 2)

print(Result)