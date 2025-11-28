#Brute Force Attack
#Kcijo Galapate




password = "12345" #vreated a variable called password with "12345" as its value

max_attempts = 5 #stated the up to amount it can get to
attempts = 0 #created base for the attempts 

print("---------------User Password--------------")
while attempts < max_attempts: #stating while attempts is less than maximum attempts
    enter = input("Enter password:") #user input
  #using if else statement  
    if enter == password: #checking if user input (enter) is the same as password using ==
      print("Password is Correct!")
      break #stopping the program if the condition is true
    else:
        attempts += 1 #incrementing attempts based on how many the user has already tried
        remaining = max_attempts - attempts #decreasing 1 each attempt the user made
        if remaining > 0: #if the user reached 0 attempts 
         print("Incorrect password. You have", remaining, "attempts left.")
        else:
           print("Maximum attempts have been reached. Authorities have been alerted!")
        
