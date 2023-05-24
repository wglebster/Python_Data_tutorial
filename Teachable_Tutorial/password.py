PASSWORD = "falcon12345"

for i in range(3):
    attempt = input("Enter password: ")
    if attempt != PASSWORD:
        print("Access denied")
        attempt
    else:
        print("Greetings Professor Falcon")