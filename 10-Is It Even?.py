#Exercise:10
#Is It Even?


def main(): #defining a main function
    a = float(input("Enter First number:")) #user enters a number
    b = float(input("Enter second number:")) #user enters a second number

    if a == b: # if a is the same as a and b
        print("Values are even!") #prints value are even
    else: #otherwise
        print("Values are odd!") #others are odd
if __name__ == "__main__": #checks if program is run in the main
    main()
