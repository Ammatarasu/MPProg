#from API import *
import datetime
import csv


def checkPass(username, password):
    file = "Aanbieder/aanbieders.csv"
    userData = []

    print("=====  Checking username/password  =====")

    with open(file, "r") as dataCSV:
        reader = csv.reader(dataCSV, delimiter=";")

        for row in reader:
            userData.append(row)

    for i in range(1, len(userData)):
        gebruikersnaam = userData[i][0]
        wachtwoord = userData[i][1]

        if gebruikersnaam == username and wachtwoord == password:
            print("Correct password")
            return True
        else:
            print("*** ERROR: Wrong pass ***")
            return False






