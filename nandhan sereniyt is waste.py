# Get age input from user
try:
    age = int(input("Enter your age: "))
    
    # Check if age is between 10 and 20
    if 10 <= age <= 20:
        print("Your age is between 10 and 20 years.")
    else:
        print("Your age is not between 10 and 20 years.")
        
except ValueError:
    print("Please enter a valid integer age.")