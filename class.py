"""age = input("Enter an age")"""
#print("are they eligable for work?", age > 18 and age < 68)

strong_password=input("Please enter a secure password")
if len(strong_password > 8) and len(strong_password <12):
    print("Please enter a stronger password!")
else:
    print("Congratulations! You have entered a strong password!")



    user = int(input("enter a password"))
    if user < 8 or user > 12:
        print("does not meet length criteria")
    else:
        print("congrats!")



    age = int(input("Enter a number"))
    if age >= 18:
        print("You are old enough")
    else:
        print("Sorry, you are not old enough yet.")
