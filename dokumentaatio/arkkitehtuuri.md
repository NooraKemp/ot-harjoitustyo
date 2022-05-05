# Arkkitehtuurikuvaus

## Rakenne
Ohjelman koodin pakkausrakenne:

![pakkauskaavio](https://github.com/NooraKemp/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/pakkauskaavio.png)

Pakkaus "services" sisältää sovelluslogiikasta vastaavan koodin. Pakkauksessa "sprites" on luokkia, jotka kuvaavat sprite-oloita ja "entites" kuvia, joita spritet käyttävät. Tietojen pysyväistallennuksesta vastaava koodi on pakkauksessa "repositories". Näkymiin liittyvä koodi on pakkauksessa "ui.

## Tietojen pysyväistallennus
Luokka LeaderboardRepository huolehtii tietojen tallentamisesta SQLite-tietokantaan. Pelissä saadut pisteet tallennetaan Leaderboard-tauluun. Taulu alustetaan initialize_database.py-tiedostossa.

## Käyttöliittymä
Käyttöliittymässä on kolme näkymää:
- Aloitusnäkymä
- Pelinäkymä
- Pelinpäättymisnäkymä

Käyttöliittymä on pyritty erottamaan sovelluslogiikasta. Näkymät on toteutettu omina luokkinaan Ui-hakemistoon ja niiden näyttämisestä vastaa Renderer-luokka.

## Toiminnallisuudet
### Avaruusaluksen laserin ampuminen
Kun pelaaja ampuu avaruusaluksen laserin, sovelluksen toiminta etenee seuraavalla tavalla:

![laserin_ampuminen](https://github.com/NooraKemp/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/laserin_ampuminen.png)

Pelaaja painaessa välilyöntinäppäintä tarkistetaan ensin koska avaruusalus on viimeksi ampunut laserin. Mikäli edellistä ampumisesta on kulunut riittävästi aikaa spaceship_can_shoot_laser palauttaa arvon True. Ryhmään spaceship_lasers lisätään uusi Laser, joka sijainti peliruudulla määrittyy avaruusaluksen sijainnin mukaan. Avaruusaluksen last_shoot_time aika päivitetään.

# Rakenteeseen jääneet heikkoudet
Gameloop-luokan olisi voinut toteuttaa eri tavalla, jotta sen testaaminen olisi ollut helpompaa. Nyt sen testaaminen jäi vähäiseksi. Luokissa Gameloop ja Game on liikaa attribuutteja.
