#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

print("Welcome to our Calculator")
bill=float(input("What is the total bill\n" ))
tip=int(input("what pecentage? 12,15,18 \n"))
people=int(input("To be share among how many people? \n"))
tip_in_pecentage=tip/100
total_bill_amount=bill*tip_in_pecentage
total_amount_per_person=total_bill_amount/people

print(f"each person will pay {total_amount_per_person} bill",2 )