#from API import *
import datetime
import csv

csvFile = "Aanbieder/aanbieders.csv"


def checkPass(username, password):
    userData = []

    print("=====  Checking username/password  =====")

    with open(csvFile, "r") as aanbiedersCSV:
        reader = csv.reader(aanbiedersCSV, delimiter=";")

        for row in reader:
            userData.append(row)

    print(userData)
    for i in range(1, len(userData)):
        gebruikersnaam = userData[i][0]
        wachtwoord = userData[i][1]

        usernameList = []
        usernameList.append(gebruikersnaam)

        if gebruikersnaam == username and wachtwoord == password:
            print("* Correct password")
            return True
        else:
            print("*** ERROR: Wrong pass ***")


def checkAvailable(username):
    usernames = []

    print("=====  Checking if username is available  =====")

    with open(csvFile, "r") as aanbiedersCSV:
        reader = csv.reader(aanbiedersCSV, delimiter=";")
        for row in reader:
            usernames.append(row[0])

    if username in usernames:
        print("*** ERROR: username already in use ***")
        return "400"
    else:
        print("* Username not in use")
        return True


def newUser(username, password, seatcount):
    print("=====  Trying to add user to file  =====")
    with open(csvFile, "a", newline='') as aanbiedersCSV:
        writer = csv.writer(aanbiedersCSV, delimiter=";")

        isAvailable = checkAvailable(username)
        userData = (username, password, seatcount)

        if isAvailable == True:
            print("* Adding user to {}".format(csvFile))
            writer.writerow(userData)
            return True
        else:
            print("*** New user not added ***")
