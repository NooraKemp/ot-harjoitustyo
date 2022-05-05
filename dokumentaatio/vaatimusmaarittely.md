# Vaatimusmäärittely

## Sovelluksen tarkoitus
Sovellus on Space Invaders-tyylinen peli. Pelin tarkoituksena on saada kerättyä mahdollisimman paljon pisteitä tuhoamalla vihollisia.

## Käyttäjät
Sovelluksella on vain yhden tyyppisiä käyttäjiä (pelaajat).

## Käyttöliittymä
Käyttöliittymässä on kolme näkymää: aloitus-, peli - ja pelinpäättymisnäkymät.

### Aloitusnäkymä
Aloitusnäkymässä ruudulla on teksti "MAIN MENU" sekä kaksi painiketta.

Painikkeet:
- "PLAY": Aloittaa pelin.
- "QUIT": Sulkee sovelluksen.

### Pelinäkymä
- Pelinäkymän alalaidassa on avaruusalus, joka on pelaajan pelihahmo.
- Ruudun on vihollisia, jotka liikkuvat oikealle ja vasemmalle. 
- Kun joku vihollisista osuu ruudun reunaan, kaikki viholliset liikkuvat ruudulla alaspäin sekä vaihtavat liikkumissuuntaa.
- Ruudun vasemmassa yläkulmassa näkyy pelaajan pistemäärä sekä elämien määrä.
- Ruudun oikeassa yläkulmassa näkyy korkein pelissä saatu pistemäärä.

### Pelinpäättymisnäkymä
Pelinpäättymisnäkymässä ruudulla on teksti "GAME OVER" sekä kolme painiketta.

Painikkeet:
- "PLAY": Aloittaa uuden pelin.
- "QUIT": Sulkee sovelluksen.
- "MAIN MENU": Palaa aloitusnäkymään.

## Perusversion toiminnallisuudet

### Ennen pelin alkua
Aloitusnäkymässä ruudulla on painike "Play", jota painamalla pelaaja pääsee pelaamaan peliä.

### Pelaaminen
- Pelaaja liikuttaa ruudun alareunassa olevaa avaruusalusta, joka voi liikkua oikealla ja vasemmalle.
- Pelaaja ampuu vihollisia lasereilla tarkoituksenaan tuhota niitä.
- Pelaaja väistelee vihollisten ampumia lasereita.
- Vihollisten tuhoaminen kasvattaa pelaajan pistemäärää.
- Vihollisen laserin osuminen pelaajaa vähentää yhden elämän.
- Jos pelaaja saa tuhottua kaikki viholliset, ruudulle ilmestyy uusi vihollisjoukko.

### Pelin päättyminen
- Peli päättyy, kun pelaajan avaruusalus tuhoutuu eli kun elämien määrä on nolla.
- Viholliset liikkuvat peliruudulla alaspäin ja peli päättyy myös, jos joku niistä osuu peliruudun alareunaan.
- Pelin päätyttyä siirrytään pelinpäättymisnäkymään ja ruudulle tulee näkyviin teksti "Game over" sekä pelaajan pistemäärä.

## Jatkokehitysideat
Perusversion lisäksi sovelluksessa voisi olla myös seuraavat toiminnallisuudet:
- Top 10 lista korkeimmista pelissä saavutetuista pisteistä
- Vihollisten liikkuminen nopeutuu sitä mukaa, kun niiden määrä vähenee.
- Ruudulle ilmestyy satunaisesti ylimääräinen vihollinen, jonka tuhoamisesta saa lisäpisteitä.
- Peliruudulla on suojakilpiä, joiden taakse avaruusalus voi piiloitua. Suojakilvet tuhoutuvat pikkuhiljaa, kun niihin osuu vihollisen lasereita.
- Pelissä on äänet.
