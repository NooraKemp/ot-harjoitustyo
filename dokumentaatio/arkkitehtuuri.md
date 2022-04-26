# Arkkitehtuurikuvaus

## Rakenne
![pakkauskaavio](https://github.com/NooraKemp/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/pakkauskaavio.png)

## Tietojen pysyväistallennus
Luokka LeaderboardRepository huolehtii tietojen tallentamisesta SQLite-tietokantaan. Pelissä saadut pisteet tallennetaan Leaderboard-tauluun. Taulu alustetaan initialize_database.py-tiedostossa.
