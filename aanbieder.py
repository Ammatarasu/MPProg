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

    try:
        for i in range(1, len(userData)):
            gebruikersnaam = userData[i][0]
            wachtwoord = userData[i][1]

            usernameList = []
            usernameList.append(gebruikersnaam)

            if gebruikersnaam == username and wachtwoord == password:
                print("* Correct password")
                return True
            else:
                print("*** NO MATCH")
    except IndexError:
        print("*** ERROR: Wrong password ***")


def checkAvailable(username):
    usernames = []

    print("=====  Checking if username is available  =====")

    try:
        with open(csvFile, "r") as aanbiedersCSV:
            reader = csv.reader(aanbiedersCSV, delimiter=";")
            for row in reader:
                usernames.append(row[0])

        if username in usernames:
            print("*** ERROR: username already in use ***")
            return 400
        else:
            print("* Username not in use")
            return True

    except IndexError:
        print("*** ERROR: ERROR WHILE READING *** ")
        return 409


def newUser(username, password, seatcount):
    print("=====  Trying to add user to file  =====")
    with open(csvFile, "a", newline='') as aanbiedersCSV:
        writer = csv.writer(aanbiedersCSV, delimiter=";")

        isAvailable = checkAvailable(username)
        userData = (username, password, seatcount)

        if isAvailable:
            print("* Adding user to {}".format(csvFile))
            writer.writerow(userData)
            return True
        elif isAvailable == 400:
            print("*** New user not added ***")
            return 400
        elif isAvailable == 409:
            return 409
        else:
            print("*!* UNKNOWN ERROR *!*")

# Heisenberg
