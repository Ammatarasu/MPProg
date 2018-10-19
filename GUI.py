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
#root.geometry("480x270")

# === Hoofd menu instellen ===
# Look hoofd menu
knopKleurM = "white"
knopTekstM = "black"

labelKleur = "red"
labelTekst = "black"

frameAchtergrond = "red"

# Hoofd frame bouwen
mainFrame = Frame(master=root, width=480, height=270)
mainFrame.pack(fill="both", expand=True)

# Knoppen voor de verschillende schermen
allFilms = Button(master=mainFrame, command=toonAllFilms,bg=knopKleurM, fg=knopTekstM, text="Alle films")
allFilms.grid(row=0, column=0, ipadx=5, sticky=N)
ticketKopen = Button(master=mainFrame, command=toonTicket, bg=knopKleurM, fg=knopTekstM, text="Ticket kopen")
ticketKopen.grid(row=0, column=1, ipadx=5)
biosStarten = Button(master=mainFrame, command=toonAanbiedersLoginScherm, bg=knopKleurM, fg=knopTekstM, text="Bioscoop starten")
biosStarten.grid(row=0, column=2, ipadx=5)
infoFrame = Button(master=mainFrame, command=toonInfo, text="?")
infoFrame.grid(row=3, column=2, sticky=E)

# Labeltje
welcomeLabel = Label(master=mainFrame, bg=labelKleur, fg=labelTekst, text="Welkom :)")
welcomeLabel.grid(row=2, column=0, columnspan=3, pady=20)

# === Menu waar je alle films kunt zien ===
allFilmFrame = Frame(master=root)
mainFrame.pack(fill="both", expand=True)

# === Menu waar gebruiker ticket kan kopen ===
ticketFrame = Frame(master=root)
ticketFrame.pack(fill="both", expand=True)

# === Menu waar aanbieder inlogt ===
aanbiedersLoginFrame = Frame(master=root)
aanbiedersLoginFrame.pack(fill="both", expand=True)
# Knoppen
terugButton = Button(master=aanbiedersLoginFrame, text="Terug", command=toonMain)
terugButton.grid(row=0, column=0, padx=5, pady=5)
inlogKnop = Button(master=aanbiedersLoginFrame, text="Login", command=aanbiedersLogin)
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
aanbiedersFrame = Frame(master=root)
aanbiedersFrame.pack(fill="both", expand=True)
# Labels
welkomLabel = Label(master=aanbiedersFrame, fg=labelTekst)
welkomLabel.grid(row=0, column=1, padx=10, pady=5)
# Knoppen
logoutKnop = Button(master=aanbiedersFrame, text="Uitloggen", command=toonAanbiedersLoginScherm)
logoutKnop.grid(row=0, column=0, padx=5, pady=5)
rentFilm = Button(master=aanbiedersFrame, text="Film aanbieden")
rentFilm.grid(row=1, column=1, sticky=W)
rentedFilms = Button(master=aanbiedersFrame, text="Aangeboden films")
rentedFilms.grid(row=1, column=2, sticky=W)
# Invoer velden

# === Info frame ===
infoFrame = Frame(master=root)
infoFrame.pack(fill="both", expand=True)



toonMain()
root.mainloop()

