# Vaatimusmäärittely

## Sovelluksen tarkoitus
Sovellus on Space Invaders-tyylinen peli. Pelin tarkoituksena on saada kerättyä mahdollisimman paljon pisteitä.

## Käyttäjät
Sovelluksella on vain yhden tyyppisiä käyttäjiä (pelaajat).

## Käyttöliittymäliuonnos
- Käyttölittymässä on kolme näkymää: aloitus-, peli - ja pelinpäättymisnäkymät.
- Pelinäkymän alalaidassa on avaruusalus, joka on pelaajan pelihahmo. 
- Ruudun keskivaiheilla on vihollisia, jotka liikkuvat oikealle ja vasemalle, vaihtaen suuntaa, kun ne osuvat ruudun reunaan.
- Ruudun vasemmassa yläkulmassa näkyy pelaajan pistemäärä sekä elämien määrä.
- Ruudun oikessa yläkulmassa näkyy korken pelissä saatu pistemäärä.

## Perusversion toiminnallisuudet

### Ennen pelin alkua
Ruudulla on painike "Play", jota paimalla pelaaja pääsee pelaamaan peliä.

### Pelaaminen
- Pelaaja liikuttaa ruudun alareunassa olavaa avaruusalusta, joka voi liikkua oikealla ja vasemmalle.
- Pelaaja ampuu vihollisia laserilla tarkoituksenaan tuhota niitä.
- Pelaaja väistetelee vihollisten ampumia lasereita.
- Vihollisten tuhoaminen kasvattaa pelaajan pistemäärää.
- Vihollisen laserin osuminen pelaajaa vähentää yhden elämän.
- Jos pelaaja saa tuhottua kaikki viholliset, ruudulle ilmestyy uusi vihollisjoukko.

### Pelin päättyminen
- Peli päättyy, kun pelaajan avaruusalus tuohoituu eli kun elämien määrä on nolla.
- Pelin päätyttyä ruudulle tulee näkyviin teksti "Game over" sekä pelaajan pistemäärä.

## Jatkokehitysideat
Perusversion lisäksi sovelluksessa voi olla myös seuraavat toiminnallisuudet:
- Top 10 lista korkeimmista pelissä saavutetuista pisteistä
- Viholliset liikkuvat peliruudulla alaspäin ja peli päättyy myös, jos joku niistä pääsee peliruudun alareunaan.
- Vihollisten liikkuminen nopeutuu sitä mukaa, kun niiden määrä vähenee.
- Ruudulle ilmestyy satunaisesti ylimääräinen vihollinen, jonka tuhoamisesta saa lisäpisteitä.
- Peliruudulla on suojakilpiä, joiden taakse avaruusalus voi piiloitua. Suojakilvet tuhoutuvat pikkuhiljaa, kun niihin osuu vihollisen lasereita.
- Pelissä on äänet.
