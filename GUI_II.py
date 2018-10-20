from tkinter import*
from tkinter.messagebox import showinfo
from aanbieder import *

#bgKleur = "#d10e0e"
bgKleur = "#e0e1e2"

labelTekst = "#3d3d3d"
labelKleur = "#7c0000"
labelFont = "Arial 12 bold"

knopRelief = RAISED
knopKleur = "#5e5e5e"
knopTekst = "#e2e2e2"
knopFont = "Arial 12 bold"
knopWidth = 15

def hoofdMenu():
    infoFrame.pack_forget()
    aanbiederLoginFrame.pack_forget()
    aanbiederFrame.pack_forget()

    hoofdFrame.pack(fill="both", expand=True)

    # Knop om naar het filmoverzicht menu te gaan
    filmoverzichtKnop = Button(master=hoofdFrame, command=filmOverzicht, text="Film overzicht",
                               bg=knopKleur, fg=knopTekst, font=knopFont, relief=knopRelief, width=knopWidth)
    filmoverzichtKnop.grid(row=0, column=0, padx=1)
    # Knop om naar het ticket menu te gaan
    ticketKnop = Button(master=hoofdFrame, command=ticketMenu, text="Ticket kopen",
                        bg=knopKleur, fg=knopTekst, font=knopFont, relief=knopRelief, width=knopWidth)
    ticketKnop.grid(row=0, column=1, padx=1)
    # Knop om naar het aanbieder menu te gaan
    aanbiederKnop = Button(master=hoofdFrame, command=aanbiederLogin, text="Aanbieders",
                           bg=knopKleur, fg=knopTekst, font=knopFont, relief=knopRelief, width=knopWidth)
    aanbiederKnop.grid(row=0, column=2, padx=1)
    # Knop om info van het programma te laten zien
    infoKnop = Button(master=hoofdFrame, command=infoScherm, text="?",
                           bg=knopKleur, fg=knopTekst, font=knopFont, relief=knopRelief)
    infoKnop.grid(row=3, column=2, ipadx=4, sticky=E)

    # Welkom label
    welkomLabel = Label(master=hoofdFrame, text="Welkom bij skeere netflix",
                        bg=labelKleur, fg=labelTekst, font=knopFont, relief=FLAT)
    welkomLabel.grid(row=1, column=0, columnspan=3, pady=20)


def infoScherm():
    hoofdFrame.pack_forget()
    infoFrame.pack(fill="both", expand=True)

    # Knoppen
    terugKnop = Button(master=infoFrame, command=hoofdMenu, text="Terug",
                       bg=knopKleur, fg=knopTekst, font=knopFont, relief=knopRelief)
    terugKnop.grid(row=0, column=0, padx=5, pady=5)
    # Info
    creatorLabel = Label(master=infoFrame, text="Gemaakt door:",
                         bg=labelKleur, fg=knopTekst, font=knopFont)
    creatorLabel.grid(row=1, column=1)

    versieLabel = Label(master=infoFrame, text="Versie: 0.1",
                         bg=labelKleur, fg=knopTekst, font=knopFont)
    versieLabel.grid(row=2, column=1)


def filmOverzicht():
    pass


def ticketMenu():
    pass


def aanbiederLogin():
    hoofdFrame.pack_forget()
    aanbiederLoginFrame.pack(fill="both", expand=True)

    Font = "Arial 10 bold"

    # Knoppen
    terugKnop = Button(master=aanbiederLoginFrame, command=hoofdMenu, text="Terug",
                       bg=knopKleur, fg=knopTekst, font=knopFont, relief=knopRelief)
    terugKnop.grid(row=0, column=0, padx=5, pady=5, sticky=W)

    loginKnop = Button(master=aanbiederLoginFrame, command=loginCheck, text="Login",
                       bg=knopKleur, fg=knopTekst, font=Font, relief=RAISED, width=22)
    loginKnop.grid(row=3, column=2, padx=2, sticky=N)

    newUserKnop = Button(master=aanbiederLoginFrame, command=newUser, text="Nieuwe gebruiker",
                         bg=knopKleur, fg=knopTekst, font=knopFont, relief=knopRelief, width=20)
    newUserKnop.grid(row=0, column=1, columnspan=3, padx=0, pady=5, sticky=W)
    # Label
    userLabel = Label(master=aanbiederLoginFrame, text="Gebruikersnaam",
                      bg=bgKleur, fg=labelTekst, font=Font)
    userLabel.grid(row=1, column=1, sticky=E, pady=5, padx=5)

    passLabel = Label(master=aanbiederLoginFrame, text="Wachtwoord",
                      bg=bgKleur, fg=labelTekst, font=Font)
    passLabel.grid(row=2, column=1, sticky=E, pady=5, padx=5)


def aanbiederMenu():
    aanbiederLoginFrame.pack_forget()
    aanbiederFrame.pack(fill="both", expand=True)

    # Knoppen
    terugKnop = Button(master=aanbiederFrame, command=hoofdMenu, text="Uitloggen",
                       bg=knopKleur, fg=knopTekst, font=knopFont, relief=knopRelief)
    terugKnop.grid(row=0, column=0, padx=5, pady=5, sticky=W)
    # Labels
    welkomLabel = Label(master=aanbiederFrame)
    welkomLabel.grid(row=0, column=1, pady=5)


def loginCheck():
    username = userEntry.get()
    password = passEntry.get()
    loginCheck = checkPass(username, password)

    welcomeMessage ="Welkom {}".format(username)

    if loginCheck:
        aanbiederMenu()
        welkomLabel = Label(master=aanbiederFrame, text=welcomeMessage,
                            fg="black", bg=bgKleur, font="Arial 12")
        welkomLabel.grid(row=0, column=1, pady=5)
    else:
        errorMessage = "Gebruikersnaam/wachtwoord is incorrect"
        showinfo(title="Error 404", message=errorMessage)


def newUser():
    pass


root = Tk()
root.title("Skeere Netflix")
root.geometry("480x270")

hoofdFrame = Frame(master=root, bg=bgKleur)
infoFrame = Frame(master=root, bg=bgKleur)
aanbiederLoginFrame = Frame(master=root, bg=bgKleur)
aanbiederFrame = Frame(master=root, bg=bgKleur)

# Entry
userEntry =Entry(master=aanbiederLoginFrame, font=knopFont)
userEntry.grid(row=1, column=2)
passEntry = Entry(master=aanbiederLoginFrame, font=knopFont, show="■")
passEntry.grid(row=2, column=2)

hoofdMenu()
root.mainloop()