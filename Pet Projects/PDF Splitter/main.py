from pypdf import PdfReader, PdfWriter, PageObject
import re
import os
from typing import Dict, List, Optional


# Сопоставление префикса и названия теста для определенного наименования файлов
prefixes = {'Аллергокомплекс Респираторный': 'PROTRESP',
            'Аллергокомплекс Пищевой': 'PROTFOOD',
            'Аллергокомплекс Расширенный': 'PROTEXT91'}


def find_prefix(page: PageObject) -> Optional[str]:
    """Определяет название теста на PDF-странице и возвращает соответствующий префикс.

    :param page: Страница, извлеченная из PDF-файла
    """
    text = page.extract_text()
    test_prefix = ''
    for test_name in prefixes:
        if test_name in text:
            test_prefix = prefixes[test_name]
            break
    return test_prefix


def write_pages_to_file(pages_to_write: Dict[str, List[PageObject]], order_num: str) -> None:
    """Сохраняет страницы из PDF-файла как отдельные файлы с соответствующими префиксами.
    Сохранение происходит в отдельную папку, чтобы не перезаписался исходный файл.

    :param pages_to_write: Словарь с префиксами и страницами, извлеченными из PDF-файла
    :param order_num:  Номер заказа
    """
    for prefix, pages in pages_to_write.items():
        writer = PdfWriter()
        for page in pages:
            writer.add_page(page)
        with open(os.path.join(r'.\out', f'{prefix} {order_num}.pdf'), "wb") as f:
            writer.write(f)


# Имя файла для нарезки - для тестирования прописан напрямую
file_name = 'PROTFOOD 1044112883.pdf'
order_number: str = re.search(r'\d+', file_name).group()

file_reader = PdfReader(file_name)

# Создание папки для нарезанных файлов
if not os.path.isdir(r'.\out'):
    os.mkdir(r'.\out')

# Если файл состоит из одной страницы - его обработка не требуется
if file_reader.get_num_pages() > 1:
    prefix_pages: Dict[str, List[PageObject]] = {}
    for pdf_page in file_reader.pages:
        file_prefix = find_prefix(pdf_page)
        if not file_prefix:
            raise ValueError('Префикс не найден!')
        prefix_pages[file_prefix] = prefix_pages.get(file_prefix, []) + [pdf_page]

    # Если в файле только одна услуга, обработка файла не требуется
    if len(prefix_pages) > 1:
        write_pages_to_file(prefix_pages, order_number)
    else:
        print('Файл содержит только одну услугу. Обработка не требуется')

    # for pdf_page in file_reader.pages:
    #     file_prefix = find_prefix(pdf_page)
    #     write_page(pdf_page, file_prefix, order_number)
else:
    print('Файл состоит из одной страницы. Обработка не требуется')
