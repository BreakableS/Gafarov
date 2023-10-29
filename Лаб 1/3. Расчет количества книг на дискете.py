volume_disket = 1.44 * 1024 * 1024
number_of_pages = 100
number_of_lines = 50
number_of_characters_per_line = 25
single_character_code = 4
volume_book = (single_character_code * number_of_characters_per_line * number_of_lines * number_of_pages)
number_of_books = round(volume_disket // volume_book)

print("Количество книг, помещающихся на дискету:", number_of_books)
