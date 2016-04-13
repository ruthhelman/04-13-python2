# Prompt the user for an Initial Balance (and save to a variable)
# use the float() function to convert the input into a number.

balance = float(input("What is your Initial Balance? "))


# Prompt the user for an Annual Interest % (and save to a variable)
# use the float() function to convert the input into a number

interest = float(input("What is your Annual Interest %? "))

# change the percentage number into a decimal (e.g. 6 turns into .06, 5 turns into .05, etc).
# remember to save your new value to a variable!

percentage = (interest/100)

# Prompt the user for a Number of years (and save to a variable)
# use the int() function to convert the input into an integer

year = int(input("How many years would you like to calculate? "))


# Calculate the total value following the formula.
# You can use multiple steps and variables if necessary.
# Note that n = 12

ammount = balance(1+(percentage/12))**(12*year)

# Calculate the interest earned based on the above value and the initial balance

interest_earned = ammount - balance

# Output the interest earned

print("Interest earned in "+str(years)+" years: $" + str(interest_earned))

# Output the total value

print("Total value earned in "+str(years)+" years: $"+str(ammount))

