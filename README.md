# Ohjelmistotekniikka/harjoitustyö
# Pygame Space Invaders
Sovellus on Space Invaders-tyylinen peli.

## Huomio Python-versiosta
Sovelluksen toimintaa on testattu Python 3.8 versiolla.

## Dokumentaatio
- [Vaatimusmäärittely](https://github.com/NooraKemp/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](https://github.com/NooraKemp/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)
- [Changelog](https://github.com/NooraKemp/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)
- [Arkkitehtuurikuvaus](https://github.com/NooraKemp/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)
- [Käyttöohje](https://github.com/NooraKemp/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)
- [Testausdokumentti](https://github.com/NooraKemp/ot-harjoitustyo/blob/master/dokumentaatio/testaus.md)

## Sovelluksen lataaminen
Uusimman version lähdekoodi:

[Release](https://github.com/NooraKemp/ot-harjoitustyo/releases/tag/viikko6)

## Asennus
Asenna riippuvuudet komennolla:

```
poetry install
```

Suorita alustustoimenpiteet komennolla:

```
poetry run invoke build
```

Käynnistä sovellus komennolla:

```
poetry run invoke start
```

## Komentorivitoiminnot
### Ohjelman suorittaminen:
Ohjelma suoritetaan komennolla:

```
poetry run invoke start
```

### Testaus
Testit suoritetaan komennolla:

```
poetry rin invoke test
```

### Testikattavuus
Testikattavuusraportti generoidaan komennolla:

```
poetry run invoke coverage-report
```

### Pylint
Tiedoston .pylintrc määritelmien tarkistukset suoritetaan komennolla:

```
poetry run invoke lint
```
