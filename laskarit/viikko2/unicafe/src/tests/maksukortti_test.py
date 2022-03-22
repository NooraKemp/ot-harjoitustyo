import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_saldo_on_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(10)
        self.assertEqual(str(self.maksukortti), "saldo: 0.2")

    def test_rahan_ottaminen_vahentaa_saldoa_oikein(self):
        self.maksukortti.ota_rahaa(10)
        self.assertEqual(str(self.maksukortti), "saldo: 0.0")
    
    def test_saldo_ei_muutu_jos_rahaa_ei_ole_tarpeeksti(self):
        self.maksukortti.ota_rahaa(20)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
    
    def test_rahan_ottaminen_palauttaa_true_jos_rahat_riittavat(self):
        palautus = self.maksukortti.ota_rahaa(10)
        self.assertEqual(palautus, True)
    
    def test_rahan_ottaminen_palauttaa_false_jos_rahat_eivat_riita(self):
        palautus = self.maksukortti.ota_rahaa(20)
        self.assertEqual(palautus, False)
    