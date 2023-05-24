for i in range (1, 10):
    print("Start iteration number " + str(i))

    stop = input("Stop iterating? y/n ")

    if stop == "y":
        break

    print("End iteration number" + str(i))

print("Stopped")
