from tkinter import*
from tkinter.messagebox import showinfo
from aanbieder import *
from API import *

# bgKleur = "#d10e0e"
bgKleur = "#e0e1e2"

labelTekst = "#eff7ff"
labelKleur = "#007fff"
labelFont = "Arial 12 bold"

knopRelief = RAISED
knopKleur = "#5e5e5e"
knopTekst = "#e2e2e2"
knopKleurClean = "black"
knopFont = "Arial 12 bold"
knopWidth = 15

infoFont = "Arial 9 bold"

filmtips = get(0)
filmstoday = get(1)
filmstomorrow = get(2)
highlightVandaag = get(3)


def hoofdMenu():
    infoFrame.pack_forget()
    aanbiederLoginFrame.pack_forget()
    aanbiederFrame.pack_forget()
    newUserFrame.pack_forget()
    filmoverzichtFrame.pack_forget()
    highlightedFrame.pack_forget()
    filmstodayFrame.pack_forget()
    filmstomorrowFrame.pack_forget()
    movieInfoFrame.pack_forget()
    filmtipFrame.pack_forget()

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
    hoofdFrame.pack_forget()
    highlightedFrame.pack_forget()
    filmstodayFrame.pack_forget()
    filmstomorrowFrame.pack_forget()
    movieInfoFrame.pack_forget()
    filmtipFrame.pack_forget()

    filmoverzichtFrame.pack(fill="both", expand=True)

    filmvandedagTitel = highlightVandaag[0]
    highlight = "De film van de dag is {}".format(filmvandedagTitel)

    overzichtWidth = 17

    # Knoppen
    terugKnop = Button(master=filmoverzichtFrame, command=hoofdMenu, text="Terug",
                       bg=knopKleur, fg=knopTekst, font=knopFont, relief=knopRelief)
    terugKnop.grid(row=0, column=0, padx=5, pady=5)

    highlightKnop = Button(master=filmoverzichtFrame, command=highlightedInfo, text=highlight,
                           bg="#007fff", fg="#eff7ff", font=knopFont)
    highlightKnop.grid(row=1, column=1, columnspan=3, ipadx=5, pady=5)

    filmtipKnop = Button(master=filmoverzichtFrame, command=filmtip, text="Film tips",
                      bg=knopKleur, fg=knopTekst, font=knopFont, width=overzichtWidth, relief=knopRelief)
    filmtipKnop.grid(row=2, column=1, padx=5, pady=5)

    filmtodayKnop = Button(master=filmoverzichtFrame, command=filmstodayMenu, text="Films van vandaag",
                       bg=knopKleur, fg=knopTekst, font=knopFont, width=overzichtWidth, relief=knopRelief)
    filmtodayKnop.grid(row=2, column=2, padx=5, pady=5)

    filmtomorrowKnop = Button(master=filmoverzichtFrame, command=filmstomorrowMenu, text="Films van morgen",
                       bg=knopKleur, fg=knopTekst, font=knopFont, width=overzichtWidth, relief=knopRelief)
    filmtomorrowKnop.grid(row=2, column=3, padx=5, pady=5)


def highlightedInfo():
    filmoverzichtFrame.pack_forget()
    highlightedFrame.pack(fill="both", expand=True)

    knopTekst = "black"

    titel = highlightVandaag[0]
    regisseur = "Regisseur: {}".format(highlightVandaag[2])
    jaar = "Jaar: {}".format(highlightVandaag[1])
    genre = "Genre(s): {}".format(highlightVandaag[3])
    #samenvatting = highlightVandaag[5]
    filmtipInt = highlightVandaag[10]

    if filmtipInt == "1":
        filmtip = "Deze film is een aanrader volgens imdb"
        tekstKleur = "#004f02"
    elif filmtipInt == "0":
        tekstKleur = "Red"
        filmtip = "Deze film is geen aanrader volgens imdb"

    duur = "Duur: {} minuten".format(highlightVandaag[4])

    startUnix = int(highlightVandaag[7])
    startToUnix = unixConversion(startUnix)
    endUnix = int(highlightVandaag[8])
    endToUnix = unixConversion(endUnix)

    startTime = "{} tot {} op {}".format(startToUnix[11:19], endToUnix[11:19], startToUnix[0:10])

    titelTekstKleur = "#840000"

    # Knoppen
    terugKnop = Button(master=highlightedFrame, command=filmOverzicht, text="Terug",
                       bg=knopKleur, fg=knopTekst, font=knopFont, relief=knopRelief)
    terugKnop.grid(row=0, column=0, padx=5, pady=5)
    # Labels met alle film informatie
    titelLabel = Label(master=highlightedFrame, text=titel,
                       bg=bgKleur, fg=titelTekstKleur, font=knopFont)
    titelLabel.grid(row=1, column=1, columnspan=2, pady=5, sticky=W)

    regisseurLabel = Label(master=highlightedFrame, text=regisseur,
                           bg=bgKleur, fg=knopTekst, font=infoFont)
    regisseurLabel.grid(row=2, column=1, sticky=W)

    genreLabel = Label(master=highlightedFrame, text=genre,
                       bg=bgKleur, fg=knopTekst, font=infoFont)
    genreLabel.grid(row=3, column=1, sticky=W)

    #samenvattingLabel =Label(master=highlightedFrame, text=samenvatting,
    #                         bg=labelKleur, fg=labelTekst, font=infoFont, relief=RAISED)
    #samenvattingLabel.grid(row=4, column=1, columnspan=4, rowspan=3, sticky=W)

    jaarLabel = Label(master=highlightedFrame, text=jaar,
                      bg=bgKleur, fg=knopTekst, font=infoFont)
    jaarLabel.grid(row=7, column=1, sticky=W)

    duurLabel = Label(master=highlightedFrame, text=duur,
                      bg=bgKleur, fg=knopTekst, font=infoFont)
    duurLabel.grid(row=8, column=1, sticky=W)

    timeframeLabel = Label(master=highlightedFrame, text=startTime,
                           bg=bgKleur, fg=knopTekst, font=infoFont)
    timeframeLabel.grid(row=9, column=1, sticky=W)

    filmtipLabel = Label(master=highlightedFrame, text=filmtip,
                         bg=bgKleur, fg=tekstKleur, font=infoFont)
    filmtipLabel.grid(row=10, column=1, sticky=W)


def filmtip():
    filmoverzichtFrame.pack_forget()
    filmtipFrame.pack(fill="both", expand=True)

    filmtitels = []

    currentRow = 0
    currentColumn = 1

    for i in range(0, len(filmtips)):
        currentTitel = filmtips[i][0]
        filmtitels.append(currentTitel)

    for i in range(0, len(filmtitels)):
        if currentRow <= 2:
            currentRow += 1
        else:
            currentColumn += 3
            currentRow = 1

        titel = filmtitels[i]

        movieLabel = Label(master=filmtipFrame, text=titel,
                           bg=knopKleur, fg=knopTekst, font=knopFont, width=40)
        movieLabel.grid(row=currentRow, column=currentColumn, columnspan=3)

    # Knoppen
    terugKnop = Button(master=filmtipFrame, command=filmOverzicht, text="Terug",
                       bg=knopKleur, fg=knopTekst, font=knopFont, relief=knopRelief)
    terugKnop.grid(row=0, column=0, padx=5, pady=5)

    searchKnop = Button(master=filmtipFrame, command=displayMovieInfo, text="Zoek",
                        bg=knopKleur, fg=knopTekst, font=knopFont, relief=knopRelief)
    searchKnop.grid(row=0, column=3, padx=5, pady=5)
    # Labels
    searchLabel = Label(master=filmtipFrame, text="Info over een film opzoeken:",
                        bg=bgKleur, fg="Black", font=knopFont)
    searchLabel.grid(row=0, column=1, pady=5, padx=5)


def filmstodayMenu():
    filmoverzichtFrame.pack_forget()
    filmstodayFrame.pack(fill="both", expand=True)

    filmtitels = []

    currentRow = 0
    currentColumn = 1

    for i in range(0, len(filmstoday)):
        currentTitel = filmstoday[i][0]
        filmtitels.append(currentTitel)

    for i in range(0, len(filmtitels)):
        if currentRow <= 2:
            currentRow += 1
        else:
            currentColumn +=3
            currentRow = 1

        titel = filmtitels[i]

        movieLabel = Label(master=filmstodayFrame, text=titel,
                             bg=knopKleur, fg=knopTekst, font=knopFont, width=40)
        movieLabel.grid(row=currentRow, column=currentColumn, columnspan=3)

    # Knoppen
    terugKnop = Button(master=filmstodayFrame, command=filmOverzicht, text="Terug",
                       bg=knopKleur, fg=knopTekst, font=knopFont, relief=knopRelief)
    terugKnop.grid(row=0, column=0, padx=5, pady=5)

    searchKnop = Button(master=filmstodayFrame, command=displayMovieInfo, text="Zoek",
                        bg=knopKleur, fg=knopTekst, font=knopFont, relief=knopRelief)
    searchKnop.grid(row=0, column=3, padx=5, pady=5)
    # Labels
    searchLabel = Label(master=filmstodayFrame, text="Info over een film opzoeken:",
                        bg=bgKleur, fg="Black", font=knopFont)
    searchLabel.grid(row=0, column=1, pady=5, padx=5)


def filmstomorrowMenu():
    filmoverzichtFrame.pack_forget()
    filmstomorrowFrame.pack(fill="both", expand=True)

    filmtitels = []

    currentRow = 0
    currentColumn = 1

    for i in range(0, len(filmstomorrow)):
        currentTitel = filmstomorrow[i][0]
        filmtitels.append(currentTitel)

    for i in range(0, len(filmtitels)):
        if currentRow <= 2:
            currentRow += 1
        else:
            currentColumn += 3
            currentRow = 1

        titel = filmtitels[i]

        movieLabel = Label(master=filmstomorrowFrame, text=titel,
                           bg=knopKleur, fg=knopTekst, font=knopFont, width=40)
        movieLabel.grid(row=currentRow, column=currentColumn, columnspan=3)

    # Knoppen
    terugKnop = Button(master=filmstomorrowFrame, command=filmOverzicht, text="Terug",
                       bg=knopKleur, fg=knopTekst, font=knopFont, relief=knopRelief)
    terugKnop.grid(row=0, column=0, padx=5, pady=5)

    searchKnop = Button(master=filmstomorrowFrame, command=displayMovieInfo, text="Zoek",
                        bg=knopKleur, fg=knopTekst, font=knopFont, relief=knopRelief)
    searchKnop.grid(row=0, column=3, padx=5, pady=5)
    # Labels
    searchLabel = Label(master=filmstomorrowFrame, text="Info over een film opzoeken:",
                        bg=bgKleur, fg="Black", font=knopFont)
    searchLabel.grid(row=0, column=1, pady=5, padx=5)


def displayMovieInfo():
    hoofdFrame.pack_forget()
    highlightedFrame.pack_forget()
    filmstodayFrame.pack_forget()
    filmstomorrowFrame.pack_forget()
    filmtipFrame.pack_forget()

    movieInfoFrame.pack(fill="both", expand=True)

    knopTekst = "black"

    titel = filmEntry.get()
    titel1 = filmEntry1.get()
    titel2 = filmEntry2.get()

    movieInfo = []
    try:
        for i in range(0, len(filmstoday)):
            currentTitel = filmstoday[i][0]
            if currentTitel == titel or currentTitel == titel1 or currentTitel == titel2:
                movie = filmstoday[i]
                print("* Found movie info")
                movieInfo.append(movie)
                break

        for i in range(0, len(filmstomorrow)):
            currentTitel = filmstomorrow[i][0]
            if currentTitel == titel or currentTitel == titel1 or currentTitel == titel2:
                movie = filmstomorrow[i]
                print("* Found movie info")
                movieInfo.append(movie)
                break

        for i in range(0, len(filmtips)):
            currentTitel = filmtips[i][0]
            if currentTitel == titel or currentTitel == titel1 or currentTitel == titel2:
                movie = filmtips[i]
                print("* Found movie info")
                movieInfo.append(movie)
                break

        titelDisplay = movieInfo[0][0]
        regisseur = "Regisseur: {}".format(movieInfo[0][2])
        jaar = "Jaar: {}".format(movieInfo[0][1])
        genre = "Genre(s): {}".format(movieInfo[0][3])

        filmtipInt = movieInfo[0][10]

        if filmtipInt == "1":
            filmtip = "Deze film is een aanrader volgens imdb"
            tekstKleur = "#004f02"
        elif filmtipInt == "0":
            tekstKleur = "Red"
            filmtip = "Deze film is geen aanrader volgens imdb"

        duur = "Duur: {} minuten".format(movieInfo[0][4])

        startUnix = int(movieInfo[0][7])
        startToUnix = unixConversion(startUnix)
        endUnix = int(movieInfo[0][8])
        endToUnix = unixConversion(endUnix)

        startTime = "{} tot {} op {}".format(startToUnix[11:19], endToUnix[11:19], startToUnix[0:10])

        titelTekstKleur = "#840000"

        # Knoppen
        terugKnop = Button(master=movieInfoFrame, command=filmOverzicht, text="Terug",
                       bg=knopKleur, fg=knopTekst, font=knopFont, relief=knopRelief)
        terugKnop.grid(row=0, column=0, padx=5, pady=5)
        # Labels met alle film informatie
        titelLabel = Label(master=movieInfoFrame, text=titelDisplay,
                       bg=bgKleur, fg=titelTekstKleur, font=knopFont)
        titelLabel.grid(row=1, column=1, columnspan=2, pady=5, sticky=W)

        regisseurLabel = Label(master=movieInfoFrame, text=regisseur,
                           bg=bgKleur, fg=knopTekst, font=infoFont)
        regisseurLabel.grid(row=2, column=1, sticky=W)

        genreLabel = Label(master=movieInfoFrame, text=genre,
                       bg=bgKleur, fg=knopTekst, font=infoFont)
        genreLabel.grid(row=3, column=1, sticky=W)

        jaarLabel = Label(master=movieInfoFrame, text=jaar,
                      bg=bgKleur, fg=knopTekst, font=infoFont)
        jaarLabel.grid(row=7, column=1, sticky=W)

        duurLabel = Label(master=movieInfoFrame, text=duur,
                      bg=bgKleur, fg=knopTekst, font=infoFont)
        duurLabel.grid(row=8, column=1, sticky=W)

        timeframeLabel = Label(master=movieInfoFrame, text=startTime,
                           bg=bgKleur, fg=knopTekst, font=infoFont)
        timeframeLabel.grid(row=9, column=1, sticky=W)

        filmtipLabel = Label(master=movieInfoFrame, text=filmtip,
                         bg=bgKleur, fg=tekstKleur, font=infoFont)
        filmtipLabel.grid(row=10, column=1, sticky=W)

    except IndexError:
        showinfo(title="ERROR", message="Film niet gevonden. Check op spelling en hoofdletters")
        filmOverzicht()


def ticketMenu():
    pass


def aanbiederLogin():
    # De invoervelden staan aan onderkant van het programma zodat ze toeganlijk zijn
    hoofdFrame.pack_forget()
    newUserFrame.pack_forget()
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
                         bg=labelKleur, fg=labelTekst, font=knopFont, relief=knopRelief, width=20)
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
    terugKnop = Button(master=newUserFrame, command=aanbiederLogin, text="Terug",
                       bg=knopKleur, fg=knopTekst, font=knopFont, relief=knopRelief)
    terugKnop.grid(row=0, column=0, padx=5, pady=5, sticky=W)

    createKnop = Button(master=newUserFrame, command=createUser, text="Nieuwe gebruiker aanmaken",
                        bg=labelKleur, fg=labelTekst, font=knopFont, relief=knopRelief)
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
    errorMessage2 = "ERROR: 409"
    errorMessage3 = "Onbekende fout"


    if makeUser:
        showinfo(title="Succes!", message=completeMessage)

        newuserEntry.delete(0, END)
        newpassEntry.delete(0, END)
        seatcountEntry.delete(0, END)

        newUserFrame.pack_forget()
        aanbiederLoginFrame.pack(fill="both", expand=True)

    elif makeUser == 400:
        showinfo(title="Foutmelding", message=errorMessage)
        newpassEntry.delete(0, END)
        seatcountEntry.delete(0, END)

    elif makeUser == 409:
        showinfo(title="Foutmelding", message=errorMessage2)

    else:
        showinfo(title="Foutmelding", message=errorMessage3)


root = Tk()
root.title("Skeere Netflix")
#root.geometry("480x270")

hoofdFrame = Frame(master=root, bg=bgKleur)
infoFrame = Frame(master=root, bg=bgKleur)
aanbiederLoginFrame = Frame(master=root, bg=bgKleur)
aanbiederFrame = Frame(master=root, bg=bgKleur)
newUserFrame = Frame(master=root, bg=bgKleur)
filmoverzichtFrame = Frame(master=root, bg=bgKleur)
filminfoFrame = Frame(master=root, bg=bgKleur)
highlightedFrame = Frame(master=root, bg=bgKleur)
filmstodayFrame = Frame(master=root, bg=bgKleur)
filmstomorrowFrame = Frame(master=root, bg=bgKleur)
movieInfoFrame = Frame(master=root, bg=bgKleur)
filmtipFrame = Frame(master=root, bg=bgKleur)

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

# Entry veld om film informatie op te zoeken
filmEntry = Entry(master=filmstodayFrame, font=knopFont)
filmEntry.grid(row=0, column=2, padx=5, pady=5)

filmEntry1 = Entry(master=filmstomorrowFrame, font=knopFont)
filmEntry1.grid(row=0, column=2, padx=5, pady=5)

filmEntry2 = Entry(master=filmtipFrame, font=knopFont)
filmEntry2.grid(row=0, column=2, padx=5, pady=5)


hoofdMenu()
root.mainloop()

# Heisenberg