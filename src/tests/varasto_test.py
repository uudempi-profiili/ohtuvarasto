import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    ## Uudet testit

    def test_negatiivinen_alku_saldo(self):
        testiVarasto = Varasto(5,-10)
        self.assertEqual(testiVarasto.saldo, 0)

    def test_liian_iso_alku_saldo(self):
        testiVarasto = Varasto(20, 25)
        self.assertEqual(testiVarasto.saldo, 20)

    def test_negatiivinen_tilavuus(self):
        testiVarasto = Varasto(-5,0)
        self.assertEqual(testiVarasto.tilavuus, 0)

    def test_negatiivinen_lisaa(self):
        testiVarasto = Varasto(10,5)
        testiVarasto.lisaa_varastoon(-5)
        self.assertEqual(testiVarasto.saldo, 5)

    def test_liian_suuri_lisaa(self):
        testiVarasto = Varasto(10,5)
        testiVarasto.lisaa_varastoon(10)
        self.assertEqual(testiVarasto.saldo, 10)

    def test_negatiivinen_nosto(self):
        testiVarasto = Varasto(10,5)
        testiVarasto.ota_varastosta(-5)
        self.assertEqual(testiVarasto.saldo, 5)

    def test_liian_suuri_nosto(self):
            testiVarasto = Varasto(10,5)
            testiVarasto.ota_varastosta(10)
            self.assertEqual(testiVarasto.saldo, 0)

    def test_to_string(self):
            testiVarasto = Varasto(15,10)
            self.assertEqual(str(testiVarasto), "saldo = 10, vielä tilaa 5")

            #"saldo = 10.0, vielä tilaa 5.0"


    ## Alkuperäiset testit

    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
