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