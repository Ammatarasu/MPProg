import requests
import xmltodict
import datetime


# Geeft lijst met alle informatie over de films terug
def get():
    # Lijst waar alle film info in gaat
    films = []
    filmtips = []
    filmstoday = []
    filmstomorrow = []

    today = datetime.datetime.today()
    # Data die met de API mee gaat
    dateToday = today.strftime("%d-%m-%Y")
    apiKey = "vd6mdi21s4sf169lsakfipq28pms6ykx"
    sorteer = "0" # 0 is alle films opvragen

    # De API output verwerken
    apiUrl = "http://api.filmtotaal.nl/filmsoptv.xml?apikey={}&dag={}&sorteer={}".format(apiKey, "23-10-2018", sorteer)
    response = requests.get(apiUrl)
    filmXML = xmltodict.parse(response.text)
    allFilms = filmXML["filmsoptv"]["film"]

    for i in range(0, len(allFilms)):
        current = allFilms[i]

        # Alle informatie die nodig is
        titel        = current["titel"]
        jaar         = current["jaar"]
        regisseur    = current['regisseur']
        genre        = current["genre"]
        filmduur     = current["duur"]
        samenvatting = current["synopsis"]
        imdb         = current["imdb_rating"]
        startUnix    = current["starttijd"]
        eindUnix     = current["eindtijd"]
        zender       = current["zender"]
        filmtip      = current["filmtip"]

        # Info van de API aan lijst toevoegen
        filmInfo = [titel, jaar, regisseur, genre, filmduur, samenvatting, imdb, startUnix, eindUnix, zender, filmtip]
        films.append(filmInfo)

    for i in range(0, len(films)):
        current = films[i]

        today = datetime.datetime.today()
        dateToday = today.strftime("%Y-%m-%d")

        unixConverted = unixConversion(int(current[7]))
        movieDateXX = unixConverted[0:10]
        movieDateX = unixConverted[0:9]

        imbdRating = float(current[6])

        if imbdRating > 7:
            filmtips.append(current)
            print(current[6])
            print("Aandrader volgens imdb")
        elif dateToday == movieDateX or dateToday == movieDateXX:
            current.append(filmstoday)
            print("today")
        else:
            current.append(filmstomorrow)
            print("tomorrow")



    # De output is de lijst met alle film info
    return(films)


# Zet de UNIX tijd die de API geeft om in een leesbare datum
def unixConversion(unix):
    # unix naar gewone tijd omzetten
    date = datetime.datetime.fromtimestamp(unix).isoformat()
    return date

# Heisenberg