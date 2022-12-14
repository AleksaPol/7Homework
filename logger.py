def create_new_contact(contact):
    with open('phonebook.csv', 'a', encoding='utf-8') as pb:
        pb.write(contact)


def get_phone_book():
    phone_book = []
    with open('phonebook.csv', 'r', encoding='utf-8') as pb:
        for line in pb:
            phone_book.append(line)
    return phone_book
