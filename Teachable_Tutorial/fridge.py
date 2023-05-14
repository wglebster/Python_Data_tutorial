temperature = input("Enter fridge temperatue in C: ")
temperature = float(temperature)
status = "Fridge is broken"

if temperature < 0 :
    status = "Too cold!"
elif temperature <= 4 : 
    status = "Temperature OK"
elif temperature <= 6 :
    status = "Too warm!"
else: 
    status

print(status)

