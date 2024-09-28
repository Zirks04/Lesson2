#print negative, print positive
Age = [-12,13,-14,15,-16]

Username = ["arot","alexis","darpaks","gwapings"]

for dataAge in age:
    if dataAge < 0:
        print(str(dataAge) + "negative")
    elif dataAge > 0:
        print(str(dataAge)+ "positive")

    for dataUser in username:
        if dataUser == "james":
            print("james cute")
        else:
            print("james none")