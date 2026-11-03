import unittest
from unittest.mock import Mock
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.viitegeneraattori_mock.uusi.return_value = 42

        self.varasto_mock = Mock()
        self.tuotteet = {
            1: Tuote(1, "maito", 5),
            2: Tuote(2, "leipä", 3),
        }
        self.varasto_mock.saldo.side_effect = lambda tuote_id: 10
        self.varasto_mock.hae_tuote.side_effect = self.tuotteet.get

        self.kauppa = Kauppa(
            self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock
        )

    def test_yhden_tuotteen_osto_kutsuu_tilisiirtoa_oikeilla_tiedoilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", 5
        )

    def test_kahden_eri_tuotteen_osto_kutsuu_tilisiirtoa_oikealla_summalla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", 8
        )

    def test_saman_tuotteen_kaksi_kappaletta_kutsuu_tilisiirtoa_oikealla_summalla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", 10
        )

    def test_loppu_tuote_ei_vaikuta_tilisiirron_summaan(self):
        self.varasto_mock.saldo.side_effect = lambda tuote_id: 10 if tuote_id == 1 else 0

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", 5
        )

    def test_uusi_asiointi_nollaa_edellisen_ostoksen_hinnan(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        self.assertEqual(
            self.pankki_mock.tilisiirto.call_args_list,
            [
                unittest.mock.call("pekka", 42, "12345", "33333-44455", 5),
                unittest.mock.call("pekka", 42, "12345", "33333-44455", 3),
            ],
        )

    def test_jokainen_maksu_pyytää_uuden_viitenumeron(self):
        self.viitegeneraattori_mock.uusi.side_effect = [42, 43]

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 2)
        self.assertEqual(
            self.pankki_mock.tilisiirto.call_args_list,
            [
                unittest.mock.call("pekka", 42, "12345", "33333-44455", 5),
                unittest.mock.call("pekka", 43, "12345", "33333-44455", 3),
            ],
        )

    def test_poista_korista_palauttaa_tuotteen_varastoon(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)

        self.kauppa.poista_korista(1)

        self.varasto_mock.palauta_varastoon.assert_called_once_with(self.tuotteet[1])
