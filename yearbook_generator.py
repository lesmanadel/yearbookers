import cv2
from PIL import Image, ImageDraw, ImageFont

from lib.human_data_generator import generate_human_data
from lib.text_writer import get_font_with_auto_adjusted_size

font_path_default = "assets/fonts/gabiant-regular.ttf"

def generate_human_card_sections(image, text, margin_top, font_size, boundaries_y_start, boundaries_y_end=None, font_path=font_path_default):
	boundaries_x_start = 39
	boundaries_x_end = 739

	boundaries_y_start += margin_top
	if not boundaries_y_end:
		boundaries_y_end = boundaries_y_start + font_size
	font = ImageFont.truetype(font_path, font_size)
	boundaries = (boundaries_x_start, boundaries_y_start, boundaries_x_end, boundaries_y_end)

	image.rectangle(boundaries, outline="#000")

	font = get_font_with_auto_adjusted_size(font, font_size, boundaries, text)

	image.multiline_text((boundaries[0], boundaries[1]), text, fill=(0, 0, 0), font=font)

	return boundaries_y_end


def generate_human_card(single_human):
	background = cv2.imread('assets/images/human_card_background.jpg')
	profile_picture = cv2.imread(f'assets/images/profile_pictures/{single_human.imagename}')

	profile_picture = cv2.resize(profile_picture, (700, 700))
	background[39:739, 39:739] = profile_picture

	card_filename = f'card_{single_human.name}.jpg'
	cv2.imwrite(card_filename, background)

	# Open an Image
	img = Image.open(card_filename)

	# Call draw Method to add 2D graphics in an image
	image = ImageDraw.Draw(img)

	next_boundaries_y_end = 778
	next_boundaries_y_end = generate_human_card_sections(
		image=image,
		text=single_human.name,
		margin_top=0,
		font_size=52,
		boundaries_y_start=next_boundaries_y_end,
	)

	next_boundaries_y_end = generate_human_card_sections(
		image=image,
		text=single_human.email,
		margin_top=10,
		font_size=42,
		boundaries_y_start=next_boundaries_y_end,
	)

	next_boundaries_y_end = generate_human_card_sections(
		image=image,
		text=single_human.city + ", " + single_human.country,
		margin_top=10,
		font_size=42,
		boundaries_y_start=next_boundaries_y_end,
	)

	next_boundaries_y_end = generate_human_card_sections(
		image=image,
		text=single_human.work + " @ " + single_human.company,
		margin_top=10,
		font_size=42,
		boundaries_y_start=next_boundaries_y_end,
	)

	next_boundaries_y_end = generate_human_card_sections(
		image=image,
		text="contanct me when:",
		margin_top=20,
		font_size=42,
		boundaries_y_start=next_boundaries_y_end,
	)

	next_boundaries_y_end = generate_human_card_sections(
		image=image,
		text=single_human.contactme,
		margin_top=5,
		font_size=42,
		boundaries_y_start=next_boundaries_y_end,
		boundaries_y_end=next_boundaries_y_end + 500,
	)
	# Save the edited image
	img.save(card_filename)

human_lists = generate_human_data("assets/csv_data/sample.csv")
for human in human_lists:
	print(human.name)
	print(human.imagename)
	generate_human_card(human)
