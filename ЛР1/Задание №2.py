v = 1.44 # Информационный объём дискеты (Мб)
v_byte = 1.44 * 1024 * 1024# Перевод Мб в байты
numders_page = 100 # Количество страниц в книге
numbers_lines = 50 # Число строк на странице
numbers_sym = 25 # Количесвто символов в строке
code_safe = 4 # Количесвто байтов для хранения кода одного символа

numbers_sym_one_book = numbers_sym * numbers_lines * numders_page # Количесвто символов в одной книге
v_one_book = numbers_sym_one_book * code_safe # Объём в байтах одной книги
numbers_book = round(v_byte / v_one_book) #  Количество книг, которое можно разместить на дискете

print("Количество книг, помещающихся на дискету:", numbers_book)
