# Käyttöohje
Lataa projektin lähdekoodi täältä:
[Release](https://github.com/NooraKemp/ot-harjoitustyo/releases/tag/viikko6)

## Ohjelman käynnistäminen
Asenna ensin riippuvuudet komennolla:

```
poetry install
```

Suorita sitten alustustoimenpiteet komennolla:

```
poetry run invoke build
```

Sen jälkeen sovelluksen voi käynnistää komennolla:

```
poetry run invoke start
```

## Pelin aloittaminen
Pelin aloitusnäkymä:

![mainmenu](https://github.com/NooraKemp/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/main_menu.png)

Pelin pääsee aloittamaan painamalla "Play"-painiketta.
Ohjelman voi sulkea "Quit"-painikkeella.

## Pelaaminen
Pelinäkymä:

![peli](https://github.com/NooraKemp/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/game.png)

Avaruusalus liikkuu oikealla ja vasemmalle nuolinäppäimillä. Vihollisia ammutaan välilyöntinäppäimellä.

## Pelin päätyttyä
Näkymä pelin päätyttyä:

![gameover](https://github.com/NooraKemp/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/game_over.png)

Uuden pelin voi aloittaa painamalla "Play"-painiketta.
Ohjelman voi sulkea "Quit"-painikkeella.
Takaisin aloitusnäkymään pääsee painikkeella "Main menu".

