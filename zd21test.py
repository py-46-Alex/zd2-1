#v Задача: Написать парсер epub, fb2-файлов.
# > На входе - любой файл в виде аргумента к консольной команде.
# > На выходе - список "Название книги, имя автора, название издательства, год издания".

import xml.etree.ElementTree as ET


def parse_fb2_file(filename):
    """
    Парсит FB2-файл и возвращает название книги, имя автора и жанр
    """
    # Открываем файл и читаем его содержимое
    with open(filename, "r") as file:
        contents = file.read()
    # Разбираем XML-код файла
    root = ET.fromstring(contents)
    # Находим элементы для выдачи
    title = root.find(".//{http://www.gribuser.ru/xml/fictionbook/2.0}book-title")
    author1 = root.find(".//{http://www.gribuser.ru/xml/fictionbook/2.0}author/{http://www.gribuser.ru/xml/fictionbook/2.0}first-name")
    author2 = root.find(".//{http://www.gribuser.ru/xml/fictionbook/2.0}author/{http://www.gribuser.ru/xml/fictionbook/2.0}middle-name")
    author3 = root.find(".//{http://www.gribuser.ru/xml/fictionbook/2.0}author/{http://www.gribuser.ru/xml/fictionbook/2.0}last-name")
    izd = root.find(".//{http://www.gribuser.ru/xml/fictionbook/2.0}izdatel")
    genre = root.find(".//{http://www.gribuser.ru/xml/fictionbook/2.0}genre")
    date = root.find(".//{http://www.gribuser.ru/xml/fictionbook/2.0}date")

    # Возвращаем результаты в виде словаря
    r = {
        "title": title.text if title is not None else "Книга без имени",
        "author1": author1.text if author1 is not None else "Иван",
        "author2": author2.text if author2 is not None else "Иванович",
        "author3": author3.text if author3 is not None else "Иванов",
        "genre": genre.text if genre is not None else "Проза",
        "izd": izd.text if izd is not None else "Книги-РУ-нэта",
        "date": date.text if date is not None else "2001"
    }
    # конвертируем в нужном виде для выхода
    # > На выходе - список "Название книги, имя автора, название издательства, год издания".
    result = [r.get("title"), r.get("author1") + " " + r.get("author2") + " " + r.get("author3"), r.get("izd"),r.get("date")]
    return result

if __name__ == '__main__':
    # > На входе - любой файл в виде аргумента к консольной команде.
    print(parse_fb2_file('avidreaders.ru__alaya-koroleva.fb2'))
    print(parse_fb2_file('avidreaders.ru__mycop.fb2'))