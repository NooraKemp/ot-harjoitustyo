# Arkkitehtuurikuvaus

## Rakenne
Ohjelman koodin pakkausrakenne:

![pakkauskaavio](https://github.com/NooraKemp/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/pakkauskaavio.png)

## Tietojen pysyväistallennus
Luokka LeaderboardRepository huolehtii tietojen tallentamisesta SQLite-tietokantaan. Pelissä saadut pisteet tallennetaan Leaderboard-tauluun. Taulu alustetaan initialize_database.py-tiedostossa.

## Toiminnallisuudet
### Avaruusaluksen laserin ampuminen
Kun pelaaja ampuu avaruusaluksen laserin, sovelluksen toiminta etenee seuraavalla tavalla:

![laserin_ampuminen](https://github.com/NooraKemp/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/laserin_ampuminen.png)

Pelaaja painaessa välilyöntinäppäintä tarkistetaan ensin koska avaruusalus on viimeksi ampunut laserin. Mikäli edellistä ampumisesta on kulunut riittävästi aikaa spaceship_can_shoot_laser palauttaa arvon True. Ryhmään spaceship_lasers lisätään uusi Laser, joka sijainti peliruudulla määrittyy avaruusaluksen sijainnin mukaan. Avaruusaluksen last_shoot_time aika päivitetään.
