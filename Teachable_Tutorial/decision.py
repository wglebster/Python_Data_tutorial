student = input("Are you a student? y/n")
pets = input("Do you have pets? y/n")
smoke = input("Do you smoke? y/n")

if student == "y" and pets == "n" and smoke == "n":
    print("Property available")
elif student == "n" and pets == "y" and smoke == "n":
    print("Property available")
elif student == "n" and pets == "n" and smoke == "y":
    print("Property available")
else:
    print("Property unavailable")

