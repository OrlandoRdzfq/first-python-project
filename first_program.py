while True:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    print (f"Hello {name}, you are {age}, years old.")

    if age >=18:
        print("You are an adult")
    else:
        print("You are young")
    
    again = input("Do you want to continue? (yes or no):")

    if again.lower() == "no":
       print("Goodbye!")
       break
        




    


