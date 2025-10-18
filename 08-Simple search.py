characters = ["Jake" "Zac", "Ian", "Ron", "Sam", "Dave"]
search = input("Who should you be looking for?:")
print("-------------------------------")
if search in characters and search == "Sam":
     print("Found Sam on the list!")
else:
    print("You searched the wrong name.")
