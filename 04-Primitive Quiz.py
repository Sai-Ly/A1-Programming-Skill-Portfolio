#Primitive Quiz (Advanced)
#Kcijo Galapate
#Sequential code




score = 0 #added varaibale 'score' to keep track of correct answers

ans1 = (input("1.What's the capital of france?:")) #added variable and user input to question
if ans1.lower() == "paris": #checks if the answer is correct and '.lower' allows correct answer to ignore capitalization
    print("Correct!") #print if entered correct answer
    score += 1   #adds score for each correct answer   
else: #if user input is false
    print(f"That's incorrect") #print if answer is incorrect 
#repetition of code   
ans2 = (input("\n2.What's the capital of Germany?:"))
if ans2.lower() == "berlin":
    print("Correct!")
    score += 1
else:
    print(f"That's incorrect")

ans3 = (input("\n3.What's the capital of Italy?:"))
if ans3.lower() == "rome":
    print("Correct!")
    score += 1
else:
    print(f"That's incorrect")
    
ans4 = (input("\n4.What's the capital of Finland?:"))
if ans4.lower() == "helsinki":
    print("Correct!")
    score += 1
else:
    print(f"That's incorrect")
    
ans5 = (input("\n5.What's the capital of Poland?:"))
if ans5.lower() == "warsaw":
    print("Correct!")
    score += 1
else:
    print(f"That's incorrect")
    
ans6 = (input("\n6.What's the capital of Spain?:"))
if ans6.lower() == "madrid":
    print("Correct!")
    score += 1
else:
    print(f"That's incorrect")
    
ans7 = (input("\n7.What's the capital of Sweden?:"))
if ans7.lower() == "stockholm":
    print("Correct!")
    score += 1
else:
    print(f"That's incorrect")
    
ans8 = (input("\n8.What's the capital of Netherlands?:"))
if ans8.lower() == "amsterdam":
    print("Correct!")
    score += 1
else:
    print(f"That's incorrect")
    
ans9 = (input("\n9.What's the capital of Greece?:"))
if ans9.lower() == "athens":
    print("Correct!")
    score += 1
else:
    print(f"That's incorrect")
    
ans10 = (input("\n10.What's the capital of Portugal?:"))
if ans10.lower() == "lisbon":
    print("Correct!")
    score += 1
else:
    print(f"That's incorrect")
    
print("Your total score is", score,"/10!") #states how many answers user got correct out of 10
