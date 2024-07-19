def get_font_with_auto_adjusted_size(font, starting_size, boundaries, text):
    font_size = starting_size
    size = None

    # adjusting font size to fit inside boundaries
    while (size is None or size[0] > boundaries[2] - boundaries[0] or size[1] > boundaries[3] - boundaries[1]) and font_size > 0:
        font = font.font_variant(size=font_size)
        size = font.getsize_multiline(text)
        font_size -= 1

    return font
