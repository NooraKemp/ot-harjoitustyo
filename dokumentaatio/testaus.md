# Testausdokumentti
Ohjelmaa on testattu unittestilla automatisoiduilla yksikkö- ja integraatiotesteillä sekä manuaalisesti järjestelmätason testeillä.

## Yksikkö- ja integraatiotestaus

### Sovelluslogiikka
Sovelluslogiikasta vastaavaa luokkaa Game testataan testiluokalla [TestGame](https://github.com/NooraKemp/ot-harjoitustyo/blob/master/src/tests/services/game_test.py). Testejä vasten alustetaan Game-olio.

Luokkaa GameLoop testataan testiluokalla [TestGameLoop](https://github.com/NooraKemp/ot-harjoitustyo/blob/master/src/tests/services/game_loop_test.py).

### Repositorio-luokka
Repositorio-luokkaa LeaderboardRepository testataan testiluokalla [TestLeaderboarRepository](https://github.com/NooraKemp/ot-harjoitustyo/blob/master/src/tests/repositories/leaderboard_repository_test.py). Luokkaa testataan testitiedostolla, jonka nimi on konfiguroitu tiedostossa .env.test.

### Testikattavuus
Testauksen haarautumiskattavuus on 79%:

![teskikattavuus](https://github.com/NooraKemp/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/coverage_report.png)

Testikattavuuden ulkopuolelle on jätetty pakkaus "ui" sekä tiedostot renderer.py, clock.py ja event_queue.py.

## Järjestelmätestaus
Sovelluksin järjestelmätestaus on suoritettu manuaalisesti.

### Asennus ja konfigurointi
Sovellusta on testattu asentamalla se [käyttöohjeessa](https://github.com/NooraKemp/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md) kuvatulla tavalla ja testaamalla sen toimivuutta Linux-ympäristössä.

### Toiminnallisuudet
Testauksessa on käyty läpi kaikki [vaatimusmäärittelydokumentissa](https://github.com/NooraKemp/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
 ja [käyttöohjeessa](https://github.com/NooraKemp/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md) listatut toiminnallisuudet. Sovellusta on testattu erilaisilla syötteillä hiiren ja näppäimistön avulla. 

## Sovellukseen jääneet laatuongelmat
Gameloop-luokan testaaminen jäi sen toteutustavasta johtuen vähäiseksi.
