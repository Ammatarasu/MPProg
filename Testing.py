titelLabel = Label(master=filmoverzichtFrame, text="Titel",
                         bg=knopKleur, fg=knopTekst, font=knopFont,
                       width=10, relief=SOLID, borderwidth=3)
    titelLabel.grid(row=1, column=1)

    directorLabel = Label(master=filmoverzichtFrame, text="Regisseur",
                        bg=knopKleur, fg=knopTekst, font=knopFont,
                          width=10, relief=SOLID, borderwidth=3)
    directorLabel.grid(row=1, column=2)

    channelLabel = Label(master=filmoverzichtFrame, text="Zender",
                        bg=knopKleur, fg=knopTekst, font=knopFont,
                         width=10, relief=SOLID, borderwidth=3)
    channelLabel.grid(row=1, column=3)

    startLabel = Label(master=filmoverzichtFrame, text="Begintijd",
                        bg=knopKleur, fg=knopTekst, font=knopFont,
                       width=10, relief=SOLID, borderwidth=3)
    startLabel.grid(row=1, column=4)

    endLabel = Label(master=filmoverzichtFrame, text="Eindtijd",
                        bg=knopKleur, fg=knopTekst, font=knopFont,
                     width=10, relief=SOLID, borderwidth=3)
    endLabel.grid(row=1, column=5)