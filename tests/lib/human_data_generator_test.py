from unittest import TestCase

from lib.human_data_generator import generate_human_data


class HumanDataGeneratorTest(TestCase):
    def test_human_data_generator(self):
        csv_path = "../assets/csv_data/sample.csv"
        humans = generate_human_data(csv_path)

        self.assertEqual(humans[0].name, "Asep Suadji")
        self.assertEqual(humans[0].country, "Indonesia")
        self.assertEqual(humans[0].city, "Jakarta")
        self.assertEqual(humans[0].work, "Peneliti Palugada")
        self.assertEqual(humans[0].company, "Indomaret, Alfamaret")
        self.assertEqual(humans[0].contactme, ":3")
        self.assertEqual(humans[0].imagename, "Asep Suadji.jpg")

        self.assertEqual(humans[1].name, "Budi Fasola")
        self.assertEqual(humans[1].country, "Indonesia")
        self.assertEqual(humans[1].city, "Jakarta")
        self.assertEqual(humans[1].work, "montir")
        self.assertEqual(humans[1].company, "Bengkel")
        self.assertEqual(humans[1].contactme, "reparasi barang\r\nmakan nasi")
        self.assertEqual(humans[1].imagename, "Budi Fasola.jpg")
