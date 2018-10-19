import requests
import xmltodict
import datetime

def get():
    # Lijst waar alle film info in gaat
    films = []

    today = datetime.datetime.today()
    # Data die met de API mee gaat
    date = today.strftime("%d-%m-%Y")
    apiKey = "vd6mdi21s4sf169lsakfipq28pms6ykx"
    sorteer = "0" # 0 is alle films opvragen

    # De API output verwerken
    apiUrl = "http://api.filmtotaal.nl/filmsoptv.xml?apikey={}&dag={}&sorteer={}".format(apiKey, date, sorteer)
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
    # De output is de lijst met alle film info
    return(films)

getAPI()