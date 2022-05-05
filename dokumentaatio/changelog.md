## Viikko 3

- Sovelluksen koodaus aloitettu.
- Lisätty luokka GameLoop, joka pyörittää pelisilmukkaa.
- Lisätty luokka Game, joka vastaa pelin tilan hallinnasta.
- Lisätty luokat Sprite-olioille Background (taustakuva) ja Spaceship (avaruusalus).
- Pelaaja voi liikuttaa avaruusalusta oikealle ja vasemmalle.
- Testattu avaruusaluksen liikkumista.

## Viikko 4

- Lisätty luokka Sprite-oliolle Laser.
- Avaruusalus voi ampua lasereita, jotka liikkuvat kohti ruudun yläreunaa. Laser poistetaan, kun se menee ruudun ulkopuolelle.
- Testattu laserien ampumista ja niiden liikkumista.
- Lisätty luokka Sprite-oliolle Enemy (vihollinen).
- Peliruudulla on vihollisia, jotka liikkuvat oikealle ja vasemmalle vaihtaen suuntaa osuessaan ruudun reunaan. Vaihtaessaan suuntaa viholliset liikkuvat myös ruudulla alaspäin.
- Peli loppuu, jos joku vihollisista saavuttaa ruudun alareunan.
- Testattu vihollisten liikkumista. 

## Viikko 5

- Viholliset ampuvat lasereita.
- Vihollisen laserin osuminen avaruusalukseen vähentää siltä yhden elämän.
- Peli loppuu, kun avaruusaluksen elämien määrä on nolla.
- Vihollinen tuhoutuu, kun avaruusaluksen laser osuu siihen.
- Kun kaikki viholliset on tuhottu, ruudulle ilmestyy uusi vihollisjoukko.
- Pelaajan pisteet ja elämät sekä korkein pelissä saavutettu pistemäärä näkyvät ruudulla.
- Pelin päätyessä pelaajan pisteet tallentuvat tietokantaan.

## Viikko 6
- Lisätty näkymät Main menu ja Game over.
- Main menu-näkumässä pelaaja voi aloittaa pelin klikkaamalla hiirellä ruudun kohdasta "Play".
- Pelin päättyessä aukeaa näkymä Game over, jossa näkyvät pelaajan saamat pisteet.
- Game over näkymässä voi aloitaa uuden pelin, sulkea sovelluksen tai siirtyä näkymään Main manu.
- Uuden pelin alkaessa edellinen peli resetoituu.
- Gameloop-luokan testit eivät tällä hetkellä toimi.

## Loppupalautus
- Gameloop-luokkaan lisätty yksi testi.
