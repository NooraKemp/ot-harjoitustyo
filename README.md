# Ohjelmistotekniikka/harjoitustyö
# Pygame Space Invaders
Sovellus on Space Invaders-tyylinen peli.

## Dokumentaatio
- [Vaatimusmäärittely](https://github.com/NooraKemp/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](https://github.com/NooraKemp/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)
- [Changelog](https://github.com/NooraKemp/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

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
