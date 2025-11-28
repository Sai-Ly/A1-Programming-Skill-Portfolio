#Kcijo Galapate


characters = ["Jake" "Zac", "Ian", "Ron", "Sam", "Dave"] #making a list of names with the variable named "Characters"
search = input("Who should you be looking for?:") #user input
print("-------------------------------")
if search in characters and search == "Sam": #stating that if the search (a user input) in characters ( list of names) matches Sam
     print("Found Sam on the list!") #Found Sam
else: #saying otherwise
    print("You searched the wrong name.") #Wrong name was entered
