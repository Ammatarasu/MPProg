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
knopKleurClean = "black"
knopFont = "Arial 12 bold"
knopWidth = 15

def hoofdMenu():
    infoFrame.pack_forget()
    aanbiederLoginFrame.pack_forget()
    aanbiederFrame.pack_forget()
    newUserFrame.pack_forget()

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
    # Knop om het programma af te sluiten
    quitKnop = Button(master=hoofdFrame, command=root.destroy, text="Afsluiten",
                      bg=knopKleur, fg=knopTekst, font=knopFont, relief=knopRelief)
    quitKnop.grid(row=3, column=0, sticky=W)

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
    creatorLabel = Label(master=infoFrame, text="Gemaakt door: Project Groep 5",
                         bg=labelKleur, fg=knopTekst, font=knopFont)
    creatorLabel.grid(row=1, column=1)

    versieLabel = Label(master=infoFrame, text="Versie: 0.21",
                         bg=labelKleur, fg=knopTekst, font=knopFont)
    versieLabel.grid(row=2, column=1)


def filmOverzicht():
    pass


def ticketMenu():
    pass


def aanbiederLogin():
    # De invoervelden staan aan onderkant van het programma zodat ze toeganlijk zijn
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

    newUserKnop = Button(master=aanbiederLoginFrame, command=newUserMenu, text="Nieuwe gebruiker",
                         bg=knopKleur, fg=knopTekst, font=knopFont, relief=knopRelief, width=20)
    newUserKnop.grid(row=0, column=1, columnspan=3, padx=0, pady=5, sticky=W)
    # Label
    userLabel = Label(master=aanbiederLoginFrame, text="Gebruikersnaam",
                      bg=bgKleur, fg=knopKleurClean, font=Font)
    userLabel.grid(row=1, column=1, sticky=E, pady=5, padx=5)

    passLabel = Label(master=aanbiederLoginFrame, text="Wachtwoord",
                      bg=bgKleur, fg=knopKleurClean, font=Font)
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

        userEntry.delete(0, END)
        passEntry.delete(0, END)
    else:
        errorMessage = "Gebruikersnaam/wachtwoord is incorrect"
        showinfo(title="Error 400", message=errorMessage)

        passEntry.delete(0, END)


def newUserMenu():
    # De invoervelden staan aan onderkant van het programma zodat ze toeganlijk zijn
    aanbiederLoginFrame.pack_forget()
    newUserFrame.pack(fill="both", expand=True)

    # Knoppen
    terugKnop = Button(master=newUserFrame, command=hoofdMenu, text="Terug",
                       bg=knopKleur, fg=knopTekst, font=knopFont, relief=knopRelief)
    terugKnop.grid(row=0, column=0, padx=5, pady=5, sticky=W)

    createKnop = Button(master=newUserFrame, command=createUser, text="Nieuwe gebruiker aanmaken",
                        bg=knopKleur, fg=knopTekst, font=knopFont, relief=knopRelief)
    createKnop.grid(row=4, column=1, columnspan=2, sticky=E)
    # Labels
    usernameLabel = Label(master=newUserFrame, text="Gebruikersnaam",
                          bg=bgKleur, fg=knopKleurClean, font=knopFont)
    usernameLabel.grid(row=1, column=1, padx=2, sticky=E)
    passwordLabel = Label(master=newUserFrame, text="Wachtwoord",
                          bg=bgKleur, fg=knopKleurClean, font=knopFont)
    passwordLabel.grid(row=2, column=1, padx=2, sticky=E)
    seatcountLabel = Label(master=newUserFrame, text="Uw aantal zitplaatsen",
                          bg=bgKleur, fg=knopKleurClean, font=knopFont)
    seatcountLabel.grid(row=3, column=1, padx=2, sticky=E)


def createUser():
    username = newuserEntry.get()
    password = newpassEntry.get()
    seatcount = seatcountEntry.get()

    makeUser = newUser(username, password, seatcount)

    completeMessage = "Nieuwe gebruiker {} toegevoegd".format(username)
    errorMessage = "Gebruikersnaam is al in gebruik"

    if makeUser:
        showinfo(title="Succes!", message=completeMessage)
        newuserEntry.delete(0, END)
        newpassEntry.delete(0, END)
        seatcountEntry.delete(0, END)

    else:
        showinfo(title="Foutmelding", message=errorMessage)
        newpassEntry.delete(0, END)
        seatcountEntry.delete(0, END)




root = Tk()
root.title("Skeere Netflix")
root.geometry("480x270")

hoofdFrame = Frame(master=root, bg=bgKleur)
infoFrame = Frame(master=root, bg=bgKleur)
aanbiederLoginFrame = Frame(master=root, bg=bgKleur)
aanbiederFrame = Frame(master=root, bg=bgKleur)
newUserFrame = Frame(master=root, bg=bgKleur)

# Entry velden voor aanbiederLoginFrame
userEntry = Entry(master=aanbiederLoginFrame, font=knopFont)
userEntry.grid(row=1, column=2)
passEntry = Entry(master=aanbiederLoginFrame, font=knopFont, show="■")
passEntry.grid(row=2, column=2)

# Entry velden voor newUserFrame
newuserEntry = Entry(master=newUserFrame, font=knopFont)
newuserEntry.grid(row=1, column=2)
newpassEntry = Entry(master=newUserFrame, font=knopFont)
newpassEntry.grid(row=2, column=2)
seatcountEntry = Entry(master=newUserFrame, font=knopFont)
seatcountEntry.grid(row=3, column=2)

hoofdMenu()
root.mainloop()

# Heisenberg