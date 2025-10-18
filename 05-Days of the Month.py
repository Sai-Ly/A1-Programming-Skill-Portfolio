#Kcijo Galapate
#Days of the Month (ADVANCED)



dm = { #made a dictionary named 'dm' to store data pairs
    1 : "January has 31 days", # number of month and indicated month with its days
    2 : "Febuary has 28 days", # number of month and indicated month with its days
    3 : "March has 31 days", # number of month and indicated month with its days
    4 : "April has 30 days",# number of month and indicated month with its days
    5 : "May has 31 days",# number of month and indicated month with its days
    6 : "June has 30 days", #.
    7 : "July has 31 days",#.
    8 : "August has 31 days",#.
    9 : "September has 30 days",#.
   10 : "October has 31 days",#.
   11 : "November has 30 days", #.
   12 : "December 31 days"  # number of month and indicated month with its days
}

month = int(input("Enter number of month(1-12):")) #'int()' is for codes that requires whole numbers and 'input()" for user to enter a month number
year = int (input("Enter year:")) #'int()' is for codes that requires whole numbers and 'input()" for user to enter the year

wrong = False #indicating that everything is correct for now
#use of if else statement
if month < 1 or month > 12: #if month is less than one or greater than 12 
    print("Try again! Please enter Month Number 1-12.") # shows if the entered number is wrong
    wrong = True #if stated answer is wrong it needs to be replaced with true
if year <= 0: #if year is less than or equal to zero
    print("Please enter valid year.") #requires to enter valid year
    wrong = True #if stated answer is wrong it needs to be replaced with true
    
if not wrong: #if everything goes accordingly
    if month == 2: #if the month is equals to 2 in the dictionary which is febuary
        if (year % 400 == 0) and (year % 4 == 0) or ( year != 100): #checks leap year if its divisible by 400 or 4 but not with 100
            print("Febuary has 29 days (leap year)") #print if leap year
        else:
            print("Febuary has 28 days") #if year is not leap year
    else:
        print(dm.get(month)) #returns value of the month
    
