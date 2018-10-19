# Basis schermen toegevoegd
# Fonts toevoegen
# Interactie tussen aanbieder.py aangemaakt


from tkinter import *
from tkinter.messagebox import showinfo
from aanbieder import*


def toonMain():
    mainFrame.pack()
    allFilmFrame.pack_forget()
    ticketFrame.pack_forget()
    aanbiedersLoginFrame.pack_forget()
    infoFrame.pack_forget()
    aanbiedersFrame.pack_forget()


def toonAllFilms():
    mainFrame.pack_forget()
    allFilmFrame.pack()
    ticketFrame.pack_forget()
    aanbiedersLoginFrame.pack_forget()
    infoFrame.pack_forget()
    aanbiedersFrame.pack_forget()


def toonTicket():
    mainFrame.pack_forget()
    allFilmFrame.pack_forget()
    ticketFrame.pack()
    aanbiedersLoginFrame.pack_forget()
    infoFrame.pack_forget()
    aanbiedersFrame.pack_forget()


def toonAanbiedersLoginScherm():
    mainFrame.pack_forget()
    allFilmFrame.pack_forget()
    ticketFrame.pack_forget()
    aanbiedersLoginFrame.pack()
    infoFrame.pack_forget()
    aanbiedersFrame.pack_forget()

def toonAanbieders():
    aanbiedersLoginFrame.pack_forget()
    aanbiedersFrame.pack()


def toonInfo():
    mainFrame.pack_forget()
    allFilmFrame.pack_forget()
    ticketFrame.pack_forget()
    aanbiedersLoginFrame.pack_forget()
    infoFrame.pack()
    aanbiedersFrame.pack_forget()


def huurFilm():
    pass

def aanbiedersLogin():
    username = usernameEntry.get()
    password = passwordEntry.get()
    loginCheck = checkPass(username, password)

    welcomeMessage = "Welkom {}".format(username)

    if loginCheck:
        toonAanbieders()
        welkomLabel["text"] = welcomeMessage
    else:
        errorMessage = "Gebruikersnaam/Wachtwoord klopt niet"
        showinfo(title="Error", message=errorMessage)

root = Tk()
root.title("Skeere Netflix")


# === Hoofd menu instellen ===
# Look
knopKleur = "#5e5e5e"
knopTekst = "white"

labelKleur = "black"
labelTekst = "white"

frameAchtergrond = "#d10e0e"

# Look hoofd menu

# Hoofd frame bouwen
mainFrame = Frame(master=root, bg=frameAchtergrond)
mainFrame.pack(fill="both", expand=False)

# Knoppen voor de verschillende schermen
allFilms = Button(master=mainFrame, command=toonAllFilms,bg=knopKleur, fg=knopTekst, text="Alle films")
allFilms.grid(row=0, column=0, ipadx=5, sticky=N)
ticketKopen = Button(master=mainFrame, command=toonTicket, bg=knopKleur, fg=knopTekst, text="Ticket kopen")
ticketKopen.grid(row=0, column=1, ipadx=5)
biosStarten = Button(master=mainFrame, command=toonAanbiedersLoginScherm, bg=knopKleur, fg=knopTekst, text="Bioscoop starten")
biosStarten.grid(row=0, column=2, ipadx=5)
infoFrame = Button(master=mainFrame, command=toonInfo, text="?")
infoFrame.grid(row=3, column=2, sticky=E)

# Labeltje
welcomeLabel = Label(master=mainFrame, bg=labelKleur, fg=labelTekst, text="Welkom bij Skeere Netflix")
welcomeLabel.grid(row=2, column=0, columnspan=3, pady=20)

# === Menu waar je alle films kunt zien ===
allFilmFrame = Frame(master=root, bg=frameAchtergrond)
mainFrame.pack(fill="both", expand=True)
# Knoppen
terugButton = Button(master=allFilmFrame, text="Terug", bg=knopKleur, fg=knopTekst, command=toonMain)
terugButton.grid(row=0, column=0, padx=5, pady=5)

# === Menu waar gebruiker ticket kan kopen ===
ticketFrame = Frame(master=root, bg=frameAchtergrond)
ticketFrame.pack(fill="both", expand=True)
# Knoppen
terugButton = Button(master=ticketFrame, text="Terug", bg=knopKleur, fg=knopTekst, command=toonMain)
terugButton.grid(row=0, column=0, padx=5, pady=5)

# === Menu waar aanbieder inlogt ===
aanbiedersLoginFrame = Frame(master=root, bg=frameAchtergrond)
aanbiedersLoginFrame.pack(fill="both", expand=True)
# Knoppen
terugButton = Button(master=aanbiedersLoginFrame, text="Terug", bg=knopKleur, fg=knopTekst, command=toonMain)
terugButton.grid(row=0, column=0, padx=5, pady=5)
inlogKnop = Button(master=aanbiedersLoginFrame, text="Login", bg=knopKleur, fg=knopTekst, command=aanbiedersLogin)
inlogKnop.grid(row=3, column=2, sticky=W)
# Inlog velden en labels
usernameEntry = Entry(master=aanbiedersLoginFrame)
usernameEntry.grid(row=1, column=2)
usernameLabel = Label(master=aanbiedersLoginFrame, bg=labelKleur, fg=labelTekst, text="Gebruikersnaam:")
usernameLabel.grid(row=1, column=1, sticky=E)

passwordEntry = Entry(master=aanbiedersLoginFrame, show="*")
passwordEntry.grid(row=2, column=2)
passwordLabel = Label(master=aanbiedersLoginFrame, bg=labelKleur, fg=labelTekst, text="Wachtwoord:")
passwordLabel.grid(row=2, column=1, sticky=E)

# === Scherm waar de aanbieders al hun info kunnen zien ===
aanbiedersFrame = Frame(master=root, bg=frameAchtergrond)
aanbiedersFrame.pack(fill="both", expand=True)
# Labels
welkomLabel = Label(master=aanbiedersFrame, bg=frameAchtergrond, fg=labelTekst)
welkomLabel.grid(row=0, column=1, padx=10, pady=5)
# Knoppen
logoutKnop = Button(master=aanbiedersFrame, text="Uitloggen", bg=knopKleur, fg=knopTekst, command=toonAanbiedersLoginScherm)
logoutKnop.grid(row=0, column=0, padx=5, pady=5)
rentFilm = Button(master=aanbiedersFrame, bg=knopKleur, fg=knopTekst, text="Film aanbieden")
rentFilm.grid(row=1, column=1, sticky=W)
rentedFilms = Button(master=aanbiedersFrame, bg=knopKleur, fg=knopTekst, text="Aangeboden films")
rentedFilms.grid(row=1, column=2, sticky=W)
# Invoer velden

# === Info frame ===
infoFrame = Frame(master=root, bg=frameAchtergrond)
infoFrame.pack(fill="both", expand=True)
# Knoppen
terugButton = Button(master=infoFrame, text="Terug", bg=knopKleur, fg=knopTekst, command=toonMain)
terugButton.grid(row=0, column=0, padx=5, pady=5)


toonMain()
root.mainloop()

