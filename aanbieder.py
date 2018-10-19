#from API import *
import datetime
import csv


def checkPass(username, password):
    file = "Aanbieder/aanbieders.csv"

    with open(file, "r") as dataCSV:
        reader = csv.reader(dataCSV, delimiter=";")

        for row in reader:
            if row[0] == "gebruikersnaam" and row[1] == "wachtwoord":
                pass
            else:
                if row[0] == username and row[1] == password:
                    return True
                else:
                    return False


