#BIOGRAPHY (ADVANCED)
#Kcijo Galapate


bio = {}  #making a dictionary called 'bio'
bio["name"] = input("What's your name?:") #adding a value that belongs to the key           
bio["hometown"] = input("Where are you from?:") #user input answers to the question
bio["age"] = input("How old are you?:") #user input answers to the question

print("\n===============BIO STORED================") #printing the data that's been stored
for key, value in bio.items(): #indicates loop for the key value pair
    print(f"{key}: {value}") #prints key and user input

print("-------------------------------------------")
print(f"Hello {bio["name"]} nice to meet you! I see you're from {bio["hometown"]} and you're {bio["age"]} years old!")
