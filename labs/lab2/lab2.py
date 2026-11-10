import csv
import random
import xml.dom.minidom as minidom


def get_year(date_str):
    date_clean = date_str.strip()
    if not date_clean:
        return 0
    date_part = date_clean.split()[0]
    if "." in date_part:
        year_str = date_part.split(".")[-1]
    else:
        year_str = date_part[:4]
    if year_str.isdigit():
        return int(year_str)
    return 0


def count_long_titles(books_csv):
    books_csv.seek(0)
    reader = csv.reader(books_csv, delimiter=";")
    next(reader)
    cnt = 0
    for line in reader:
        if len(line) > 1:
            title = line[1].strip()
            if len(title) > 30:
                cnt += 1
    print(f"1. Количество книг с названием длиннее 30 символов: {cnt}")


def search_books_by_author(books_csv, author_name):
    books_csv.seek(0)
    reader = csv.reader(books_csv, delimiter=";")
    next(reader)
    query = author_name.strip().lower()
    matched_books = []
    for line in reader:
        if len(line) > 3:
            author = line[2].strip().lower()
            year = get_year(line[3])
            if query in author and 0 < year <= 2016:
                matched_books.append(line)
    print(
        f"2. Найдено книг автора '{author_name}' (до 2016 года): "
        f"{len(matched_books)}"
    )
    for i, book in enumerate(matched_books[:5], start=1):
        print(f"   {i}) {book[2]} — '{book[1]}' ({get_year(book[3])} год)")


def generate_bibliography(books_csv, output_path="result.txt"):
    books_csv.seek(0)
    reader = csv.reader(books_csv, delimiter=";")
    next(reader)
    all_books = [line for line in reader if len(line) > 3]
    sample_books = random.sample(all_books, 20)
    with open(output_path, "w", encoding="utf-8") as out_file:
        for idx, book in enumerate(sample_books, start=1):
            author = book[2].strip()
            title = book[1].strip()
            year = get_year(book[3])
            line_pretty = f"{idx}. {author}. {title} - {year}\n"
            out_file.write(line_pretty)
    print(f"3. Файл '{output_path}' с 20 ссылками успешно сформирован.")


def parse_currency_xml(xml_path="currency.xml"):
    dom = minidom.parse(xml_path)
    valute_nodes = dom.getElementsByTagName("Valute")
    names = []
    values = []
    for valute in valute_nodes:
        name_node = valute.getElementsByTagName("Name")[0]
        name = name_node.firstChild.data.strip()

        value_node = valute.getElementsByTagName("Value")[0]
        val_str = value_node.firstChild.data.strip().replace(",", ".")
        val = float(val_str)

        names.append(name)
        values.append(val)
    print(f"4. XML обработан. Получено валют: {len(names)} шт.")
    print(f"   Пример Name: {names[:3]}")
    print(f"   Пример Value: {values[:3]}")
    return names, values


def get_unique_tags(books_csv):
    books_csv.seek(0)
    reader = csv.reader(books_csv, delimiter=";")
    next(reader)
    tags = set()
    for line in reader:
        if len(line) > 6 and line[6]:
            raw_tags = line[6].split("#")
            for tag in raw_tags:
                cleaned_tag = tag.strip()
                if cleaned_tag:
                    tags.add(cleaned_tag)
    print(f"Доп 1. Найдено уникальных тегов: {len(tags)}")
    print(f"       Примеры тегов: {list(tags)[:5]}")


def find_popular_books(books_csv):
    books_csv.seek(0)
    reader = csv.reader(books_csv, delimiter=";")
    next(reader)
    valid_books = [
        line for line in reader
        if len(line) > 5 and line[5].strip().isdigit()
    ]
    sorted_books = sorted(
        valid_books,
        key=lambda book: int(book[5].strip()),
        reverse=True,
    )
    top_20 = sorted_books[:20]
    print("Доп 2. Топ-20 самых популярных книг по выдачам:")
    for rank, book in enumerate(top_20, start=1):
        print(
            f"   {rank:2d}. Выдач: {book[5].strip()} | "
            f"'{book[1].strip()}' — {book[2].strip()}"
        )


if __name__ == "__main__":
    csv_filename = "C:\\pythonprojects\\labs\\lab2\\books.csv"
    xml_filename = "C:\\pythonprojects\\labs\\lab2\\currency.xml"

    with open(
        csv_filename, "r", encoding="cp1251", errors="replace"
    ) as books_csv:
        count_long_titles(books_csv)
        search_books_by_author(books_csv, "Пушкин")
        generate_bibliography(books_csv, "result.txt")
        get_unique_tags(books_csv)
        find_popular_books(books_csv)

    names_res, values_res = parse_currency_xml(xml_filename)