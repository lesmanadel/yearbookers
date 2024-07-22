import cv2
from PIL import Image, ImageDraw, ImageFont

from lib.human_data_generator import generate_human_data
from lib.text_writer import get_font_with_auto_adjusted_size
from textwrap import TextWrapper

font_path_default = "assets/fonts/gabiant-regular.ttf"
tw_name = TextWrapper(width=27, replace_whitespace=False)
tw_contactme = TextWrapper(width=40, break_long_words=False, replace_whitespace=False)
tw_work = TextWrapper(width=40, replace_whitespace=False)


def generate_human_card_sections(image, text, margin_top, font_size, boundaries_y_start, boundaries_y_end=None, font_path=font_path_default):
	boundaries_x_start = 39
	boundaries_x_end = 739

	boundaries_y_start += margin_top
	if not boundaries_y_end:
		boundaries_y_end = boundaries_y_start + font_size
	font = ImageFont.truetype(font_path, font_size)
	boundaries = (boundaries_x_start, boundaries_y_start, boundaries_x_end, boundaries_y_end)

	# image.rectangle(boundaries, outline="#000")

	font = get_font_with_auto_adjusted_size(font, font_size, boundaries, text)

	image.multiline_text((boundaries[0], boundaries[1]), text, fill=(0, 0, 0), font=font)

	return boundaries_y_end


def generate_human_card(index, single_human):
	print("[RUNNING] generating human")
	print(f'assets/images/card {int(index/6)%2} {index%6}.jpg')
	background = cv2.imread(f'assets/images/card {int(index/6)%2} {index%6}.jpg')
	try:
		profile_picture = cv2.imread(f'assets/images/profile_pictures/{single_human.imagename}')
		profile_picture = cv2.resize(profile_picture, (700, 700))
	except:
		profile_picture = cv2.imread(f'assets/images/profile_pictures/z default 5.jpg')
		profile_picture = cv2.resize(profile_picture, (700, 700))

	background = cv2.resize(background, (777, 1649))
	profile_picture = cv2.resize(profile_picture, (700, 700))
	background[39:739, 39:739] = profile_picture

	card_filename = f'assets/images/cards/card_{single_human.name}.jpg'
	cv2.imwrite(card_filename, background)

	# Open an Image
	img = Image.open(card_filename)

	# Call draw Method to add 2D graphics in an image
	image = ImageDraw.Draw(img)

	next_boundaries_y_end = 778
	next_boundaries_y_end = generate_human_card_sections(
		image=image,
		text='\n'.join(tw_name.wrap(single_human.name)),
		margin_top=0,
		font_size=70,
		boundaries_y_start=next_boundaries_y_end,
		boundaries_y_end=next_boundaries_y_end + 140,
	)

	if single_human.email:
		next_boundaries_y_end = generate_human_card_sections(
			image=image,
			text=single_human.email,
			margin_top=20,
			font_size=52,
			boundaries_y_start=next_boundaries_y_end,
		)

	if single_human.city or single_human.country:
		next_boundaries_y_end = generate_human_card_sections(
			image=image,
			text=single_human.city + ", " + single_human.country,
			margin_top=20,
			font_size=52,
			boundaries_y_start=next_boundaries_y_end,
		)

	if single_human.work or single_human.company:
		next_boundaries_y_end = generate_human_card_sections(
			image=image,
			text='\n'.join(tw_work.wrap(single_human.work + " at " + single_human.company)),
			margin_top=20,
			font_size=52,
			boundaries_y_start=next_boundaries_y_end,
			boundaries_y_end=next_boundaries_y_end + 114,
		)

	# if single_human.company:
	# 	next_boundaries_y_end = generate_human_card_sections(
	# 		image=image,
	# 		text=" at " + single_human.company,
	# 		margin_top=2,
	# 		font_size=52,
	# 		boundaries_y_start=next_boundaries_y_end,
	# 	)

	if single_human.contactme:
		next_boundaries_y_end = generate_human_card_sections(
			image=image,
			text="contanct me when:",
			margin_top=30,
			font_size=42,
			boundaries_y_start=next_boundaries_y_end,
		)

		contactme = '\n'.join(['\n'.join(tw_contactme.wrap(line))
						  for line in single_human.contactme[1:len(single_human.contactme)-1]
						 .splitlines() if line.strip() != ''])

		next_boundaries_y_end = generate_human_card_sections(
			image=image,
			text=contactme,
			margin_top=5,
			font_size=52,
			boundaries_y_start=next_boundaries_y_end,
			boundaries_y_end=next_boundaries_y_end + 400,
		)

	img.save(card_filename)


def generate_page(humans, page_number):
	print(f"[RUNNING] generating page {page_number}")
	background = cv2.imread(f'assets/images/background pattern {page_number%2}.jpg')

	top_margin = 105
	card_size_y = 1649
	row1_end = top_margin + card_size_y
	row2_end = row1_end + card_size_y

	left_margin = 74
	card_size_x = 777
	col1_end = left_margin + card_size_x
	col2_end = col1_end + card_size_x
	col3_end = col2_end + card_size_x

	coord = [
		[top_margin, row1_end, left_margin, col1_end],
		[top_margin, row1_end, col1_end, col2_end],
		[top_margin, row1_end, col2_end, col3_end],
		[row1_end, row2_end, left_margin, col1_end],
		[row1_end, row2_end, col1_end, col2_end],
		[row1_end, row2_end, col2_end, col3_end],
	]

	i = 0
	while i < len(humans):
		card2 = cv2.imread(f'assets/images/cards/card_{humans[i].imagename}')
		background[coord[i][0]:coord[i][1], coord[i][2]:coord[i][3]] = card2
		i += 1

	card_filename = f'assets/images/pages/page_{page_number}.jpg'
	cv2.imwrite(card_filename, background)


human_lists = generate_human_data("assets/csv_data/cc14.csv")

for index, human in enumerate(human_lists):
	print(human.name)
	generate_human_card(index, human)

i = 0
while i < len(human_lists):
	generate_page(humans=human_lists[i:i+6], page_number=int(i/6 + 1))
	i += 6
