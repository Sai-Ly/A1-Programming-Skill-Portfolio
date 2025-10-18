Brute Force Attack
#Kcijo Galapate




password = "12345"

max_attempts = 5
attempts = 0

print("---------------User Password--------------")
while attempts < max_attempts:
    enter = input("Enter password:")
    
    if enter == password:
      print("Password is Correct!")
      break
    else:
        attempts += 1
        remaining = max_attempts - attempts
        if remaining > 0:
         print("Incorrect password. You have", remaining, "attempts left.")
        else:
           print("Maximum attempts have been reached. Authorities have been alerted!")
        
