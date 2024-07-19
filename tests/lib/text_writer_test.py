from unittest import TestCase

from PIL import ImageFont

from lib.text_writer import get_font_with_auto_adjusted_size


class TextWriterTest(TestCase):
    def test_human_data_generator(self):
        font_path = "../assets/fonts/gabiant-regular.ttf"
        starting_size = 50
        font = ImageFont.truetype(font_path, starting_size)
        # (x-start, y-start, x-end, y-end)
        boundaries = (0, 0, 10, 15)

        text_hit_y = "A"
        font_hit_y = get_font_with_auto_adjusted_size(font, starting_size, boundaries, text_hit_y)

        self.assertEqual(font_hit_y.size, 14)

        text_hit_x = "Aaaaaaaa"
        font_hit_x = get_font_with_auto_adjusted_size(font, starting_size, boundaries, text_hit_x)

        self.assertEqual(font_hit_x.size, 2)

