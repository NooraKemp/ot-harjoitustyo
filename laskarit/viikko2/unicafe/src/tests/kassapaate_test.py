import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)
        self.rahatonkortti = Maksukortti(10)

    # Kassapäätteen luominen
    def test_luotu_kassapaate_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)
    
    def test_luodun_kassapaateen_rahamaara_on_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_myytyjen_edullisten_maara_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_myytyjen_maukkaiden_maara_oikein(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    # Edullisen lounaan ostaminen käteisellä
    def test_edullisen_kateisosto_kasvattaa_kassan_rahamaaraa_edullisen_hinnalla(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_edullisen_kateisnosto_vaihtoraha_oikein(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(500), 500-240)
    
    def test_edullisen_kateisosto_kasvattaa_edullisten_maaraa_yhdella(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_edullisen_kateisosto_kassan_rahamaaraa_ei_muutu_kun_maksu_ei_riittava(self):
        self.kassapaate.syo_edullisesti_kateisella(230)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edullisen_kateisnosto_rahat_palautetaan_kun_maksu_ei_riittava(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(230), (230))
    
    def test_edullisen_kateisosto_edullisten_maara_ei_kasva_kun_maksu_ei_riittava(self):
        self.kassapaate.syo_edullisesti_kateisella(230)
        self.assertEqual(self.kassapaate.edulliset, 0)

    # Maukkaan lounaan ostaminen käteisellä
    def test_maukkaan_kateisosto_kasvattaa_kassan_rahamaaraa_maukkaan_hinnalla(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
    
    def test_maukkaan_kateisnosto_vaihtoraha_oikein(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 500-400)
    
    def test_maukkaan_kateisosto_kasvattaa_maukkaiden_maaraa_yhdella(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_maukkaan_kateisosto_kassan_rahamaaraa_ei_muutu_kun_maksu_ei_riittava(self):
        self.kassapaate.syo_maukkaasti_kateisella(390)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukkaan_kateisnosto_rahat_palautetaan_kun_maksu_ei_riittava(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(390), (390))
    
    def test_maukkaan_kateisosto_maukkaiden_maara_ei_kasva_kun_maksu_ei_riittava(self):
        self.kassapaate.syo_maukkaasti_kateisella(390)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    # Edullisen lounaan ostaminen kortilla
    def test_edullisen_korttiosto_vahentaa_kortilta_edullisen_hinnan(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 1000-240)
    
    def test_edullisen_korttiosto_palauttaa_true(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)

    def test_edullisen_korttiosto_kasvattaa_edillisten_maaraa_yhdella(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_edullisen_korttiosto_ei_muuta_kortin_saldoa_kun_maksu_ei_riittava(self):
        self.kassapaate.syo_edullisesti_kortilla(self.rahatonkortti)
        self.assertEqual(self.rahatonkortti.saldo, 10)

    def test_edullisen_korttiosto_palauttaa_false_kun_maksu_ei_riittava(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.rahatonkortti), False)
    
    def test_edullisen_korttiosto_edullisten_maara_ei_kasva_kun_maksu_ei_riittava(self):
        self.kassapaate.syo_edullisesti_kortilla(self.rahatonkortti)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_edullisen_korttiosto_kassan_rahamaara_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    # Maukkaan lounaan ostaminen kortilla
    def test_maukkaan_korttiosto_vahentaa_kortilta_maukkaan_hinnan(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 1000-400)

    def test_maukaan_korttiosto_palauttaa_true(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)
    
    def test_maukkaan_korttiosto_kasvattaa_maukkaiden_maaraa_yhdella(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukkaan_korttiosto_ei_muuta_kortin_saldoa_kun_maksu_ei_riittava(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.rahatonkortti)
        self.assertEqual(self.rahatonkortti.saldo, 10)

    def test_maukaan_korttiosto_palauttaa_false_kun_maksu_ei_riittava(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.rahatonkortti), False)
    
    def test_maukkaan_korttiosto_maukkaiden_maara_ei_kasva_kun_maksu_ei_riittava(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.rahatonkortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_maukkaan_korttiosto_kassan_rahamaara_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    # Rahan lataaminen
    def test_kortille_lataaminen_kasvattaa_kortin_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        self.assertEqual(self.maksukortti.saldo, 1100)

    def test_negatiivisen_summan_lataaminen_kortille_ei_muuta_kortin_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)
        self.assertEqual(self.maksukortti.saldo, 1000)

    def test_kortin_lataaminen_kasvattaa_kassan_rahamaaraa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)
    
    def test_negatiivisen_summan_lataaminen_kortille_ei_muuta_kassan_rahamaaraa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    

