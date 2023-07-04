import math # This was imported from the python math library
print("\n") # create space to make output readable

'''
This is a finance calculator project. It allows users to choose beteween bond or investment.
Based on the users choice, the program will calculate either a "simple" or a "compound" interest,
and do the appropriate calculation and display the result.
In the case of a bond, the program will calculate how much a user will have to repay each
month and output the answer.
'''
# This project is built to test my skills on varriables and control structures

print("Investment -  To calculate the amount of interest you'll earn on your investment")
print("Bond -  To calculate the amount you'll have to pay on a home loan\n")

user_input = input("Enter either 'investment' or 'bond' from the menu above to proceed : ").lower() # formats all text enteries from users to lower case.

if user_input == "investment": #or user_input == "Investment" or user_input == "INVESTMENT": # Accept either of the three user_input
#All variables are presented as float values except for "years_of_investment" which is an interger value for the sake of accuracy
    amount_to_deposit = float(input("Please enter the amount you want to deposit ")) # Converts user_input to a float value
    print(f"You have deposited {amount_to_deposit} ")
    actual_interest = float(input("Enter your desired interest rate: "))/ 100
    years_of_investment = int(input("The number of years you want to invest: "))#This converts to integer
    interest_choice = input("\nEnter choice of interest. i.e compound or simple:").lower()#Prompt user for the type of interest they prefer

    #The if statement calculate simple interest if a user chooses simple
    if interest_choice == "simple": #or interest_choice == "Simple" or interest_choice == "SIMPLE": # This calculates the simple interest
        simple_interest = amount_to_deposit *(1 + actual_interest * years_of_investment)
        print(f"Your simple interest is: {simple_interest:.2f} ") #This formats the output to be in two decimal places

    #The if statement calculate compound interest if a user chooses compound
    elif interest_choice == "compound": #or interest_choice == "Compound" or interest_choice == "COMPOUND":
        compound_interest = amount_to_deposit * math.pow((1 + actual_interest), years_of_investment)
        print(f"Your compound interest is: {compound_interest:.2f} ")
   #However, if a user chooses bond, it will prompt for more questions
if user_input == "bond": #or user_input == "BOND" or user_input == "Bond": # Accept either of the three user_input
        value_of_house = float(input("Enter the value of the house:"))#Enter the value of the house
        yearly_interest_rate = float(input(f"Enter the interest rate without adding % symbol e.g 5 not 5%:"))/100
        print(f"your yearly interest rate is: {yearly_interest_rate}")
        monthly_interest_rate = yearly_interest_rate / 12 #Yearly interest divided by 12
        months_to_repay = int(input("The number of months it will take you to repay the bond:"))#The number of months it will takes you to repay
        repayment = (value_of_house * monthly_interest_rate)/(1 - (1 + monthly_interest_rate)**(- months_to_repay))#This sums up the repayment value
        print(f"The total amount to repay each month is : £{repayment:.2f}") #This will display the amount due each month for repayment.