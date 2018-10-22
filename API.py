import requests
import xmltodict
import datetime


# Geeft lijst met alle informatie over de films terug
def get(mode):
    # Lijst waar alle film info in gaat
    filmtips = []
    filmsToday = []
    filmsTomorrow = []

    filmvandedagTemp = []
    allFilms = []
    films = []

    today = datetime.datetime.today()
    # De datum van vandaag
    dateToday = today.strftime("%d-%m-%Y")
    # De datum van morgen
    tomorrow = int(today.strftime("%d")) + 1
    dateTomorrow = today.strftime("{}-%m-%Y").format(tomorrow)

    print("* Finished getting dates")

    # API key en sorteer parameter
    apiKey = "vd6mdi21s4sf169lsakfipq28pms6ykx"
    sorteer = "0" # 0 is alle films opvragen
    sorteerRecommend = "2"

    print("=====  GETTING DATA FROM API  =====")
    for i in range(0, 3):
        if i == 0:
            # De api uitvoeren om de films van vandaag te krijgen
            apiUrl = "http://api.filmtotaal.nl/filmsoptv.xml?apikey={}&dag={}&sorteer={}".format(apiKey, dateToday, sorteer)
            response = requests.get(apiUrl)
            filmXML = xmltodict.parse(response.text)
            filmstoday = filmXML["filmsoptv"]["film"]
            # Films van vandaag bij de allFilms lijst toevoegen
            allFilms.append(filmstoday)
            print("* Got movies from today")
        if i == 1:
            # De api uitvoeren om de films van morgen te krijgen
            apiUrl = "http://api.filmtotaal.nl/filmsoptv.xml?apikey={}&dag={}&sorteer={}".format(apiKey, dateTomorrow, sorteer)
            response = requests.get(apiUrl)
            filmXML = xmltodict.parse(response.text)
            filmstomorrow = filmXML["filmsoptv"]["film"]
            # Films van morgen bij de allFilms lijst toevoegen
            allFilms.append(filmstomorrow)
            print("* Got movies from tomorrow")

    # De api uitvoeren om de films van morgen te krijgen
    apiUrl = "http://api.filmtotaal.nl/filmsoptv.xml?apikey={}&dag={}&sorteer={}".format(apiKey, dateTomorrow,
                                                                                                 sorteerRecommend)
    response = requests.get(apiUrl)
    filmXML = xmltodict.parse(response.text)
    filmVanDeDag = filmXML["filmsoptv"]["film"]
    # Films van morgen bij de allFilms lijst toevoegen
    filmvandedagTemp.append(filmVanDeDag)
    print("* Got recommended movie of today")

    print("*** FINISHED FETCHING DATA FROM API ***\n")

    print("=====  PROCESSING API  =====")
    for i in range(0,2):
        day = allFilms[i]
        for i in range(0, len(day)):
            current = day[i]

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

    # filmvandedag verwerken
    current = filmvandedagTemp[0]

    # Alle informatie die nodig is
    titel = current["titel"]
    jaar = current["jaar"]
    regisseur = current['regisseur']
    genre = current["genre"]
    filmduur = current["duur"]
    samenvatting = current["synopsis"]
    imdb = current["imdb_rating"]
    startUnix = current["starttijd"]
    eindUnix = current["eindtijd"]
    zender = current["zender"]
    filmtip = current["filmtip"]

    # Info van de API aan lijst toevoegen
    filmInfo = [titel, jaar, regisseur, genre, filmduur, samenvatting, imdb, startUnix, eindUnix, zender, filmtip]
    filmvandedag = filmInfo

    print("*** FINISHED SORTING AND APPENDING WANTED INFO ***\n")

    print("=====  SORTING WANTED DATA  =====")
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
            #grade = current[6]
            #print("* Recommend according to imbdb grade over 7. Actual grade: {}".format(grade))
        elif dateToday == movieDateX or dateToday == movieDateXX:
            filmsToday.append(current)
        else:
            filmsTomorrow.append(current)

    print("*** FINISHED SORTING DATA ***\n")

    # Checken wat er teruggestuurd moet worden aan de hand van de mode
    try:
        if mode == 0:
            print("* Returning filmtips")
            return filmtips
        elif mode == 1:
            print("* Returning filmsToday")
            return filmsToday
        elif mode == 2:
            print("* Returning filmsTomorrow")
            return filmsTomorrow
        elif mode == 3:
            print("* Returning filmvandedag")
            return filmvandedag
        elif mode > 3:
            print("*** Mode {} doensn\'t exist".format(mode))
    except:
        print("*!* INPUT ERROR *!*")

# Zet de UNIX tijd die de API geeft om in een leesbare datum
def unixConversion(unix):
    # unix naar gewone tijd omzetten
    date = datetime.datetime.fromtimestamp(unix).isoformat()
    return date

# Heisenberg