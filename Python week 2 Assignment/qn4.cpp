books = {
    'Book1': 5,
    'Book2': 6,
    'Book3': 10,
}

book_name = input("Enter book name: ")

if book_name not in books:
    print("Unavailable")
else:
    while True:
        copies = input("Enter number of copies you want: ")

        if not copies.isdigit():
            print("Invalid input. Please enter a valid number.")
            continue
        
        copies = int(copies)
        break

    available = books[book_name]

    if copies <= available:
        print("Available")
    elif available > 0:
        print("Partially Available")
    else:
        print("Unavailable")
