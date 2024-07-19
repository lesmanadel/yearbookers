from unittest import TestCase

from lib.human_data_generator import generate_human_data


class HumanDataGeneratorTest(TestCase):
    def test_human_data_generator(self):
        csv_path = "/home/wo/Workspace/zdennis/yearbookers/tests/assets/csv_data/cc1410tahun.csv"
        humans = generate_human_data(csv_path)

        self.assertEqual(humans[1].name, "Asep Suadji")
        self.assertEqual(humans[1].country, "Indonesia")
        self.assertEqual(humans[1].city, "Jakarta")
        self.assertEqual(humans[1].work, "Peneliti Palugada")
        self.assertEqual(humans[1].company, "Indomaret, Alfamaret")
        self.assertEqual(humans[1].contactme, ":3")
        self.assertEqual(humans[1].imagename, "Asep Suadji.jpg")

        self.assertEqual(humans[2].name, "Budi Fasola")
        self.assertEqual(humans[2].country, "Indonesia")
        self.assertEqual(humans[2].city, "Jakarta")
        self.assertEqual(humans[2].work, "montir")
        self.assertEqual(humans[2].company, "Bengkel")
        self.assertEqual(humans[2].contactme, "reparasi barang\r\nmakan nasi")
        self.assertEqual(humans[2].imagename, "Budi Fasola.jpg")
