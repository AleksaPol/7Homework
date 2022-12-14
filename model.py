def add_new_contact():
    family = input('Введите Фамилию: ')
    name = input('Введите Имя: ')
    phone = input('Введите телефон: ')
    comment = input('Введите описание: ')
    data = family + ' ' + name + ', ' + phone + ', ' + comment
    return f'{data} \n'


def search_contact(pb, search):
    a = ''
    for el in pb:
        if el.find(search) != -1:
            a += f'{el}'
    if a == '':
        return 'Empty'
    else:
        return a


def get_search():
    return input('Введите данные контакта для поиска: ')


def mode():
    return int(input('Writing mode - 1, Search mode - 2, Exit - 0: '))
