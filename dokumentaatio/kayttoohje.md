### Käyttöohje
Lataa projektin -tähän linkki- lähdekoodi.

## Konfigurointi

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

Pelin pääsee aloittamaan klikkamalla hiirellä "Play"-painiketta.
Ohjelman voi sulkea "Quit"-painikkeella.

## Pelaaminen
Pelinäkymä:

Avaruusalus liikuu oikealla ja vasemalle nuolinäppäimillä. Vihollisia ammutaan välilyöntinäppäimellä.

## Pelin päätyttyä
Näkymä pelin päätyttyä:

Uuden pelin voi aloittaa klikkamalla hiirellä "Play"-painiketta.
Ohjelman voi sulkea "Quit"-painikkeella.
Takaisin aloitusnäkymään pääsee painikkeella "Main menu".

