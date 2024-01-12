import csv

def get_books(file_path):
    books_list = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter='|')
        header = next(reader)
        for row in reader:
            isbn, title, author, quantity, price = row
            quantity = int(quantity)
            price = float(price)
            books_list.append([isbn, title, author, quantity, price])
    return books_list

def filtered_books(books_list, keyword):
    filtered_list = []
    for book in books_list:
        if keyword.lower() in book[1].lower():
            filtered_list.append([book[0], f"{book[1]}, {book[2]}", book[3], book[4]])
    return filtered_list

def calculate_total_prices(filtered_list):
    total_prices_list = []
    for book in filtered_list:
        isbn, author, quantity, price = book
        total_price = quantity * price
        total_prices_list.append((isbn, total_price))
    return total_prices_list

file_path = "books.csv"
books_data = get_books(file_path)
print("Все книги:")
print(books_data)

keyword = "python"
filtered_books_data = filtered_books(books_data, keyword)
print(f"\nКниги с подстрокой '{keyword}' в названии:")
print(filtered_books_data)

total_prices_data = calculate_total_prices(filtered_books_data)
print("\nСписок кортежей ('isbn', quantity * price):")
print(total_prices_data)
