import model
import logger


while True:
    mode = model.mode()
    if mode == 1:
        logger.create_new_contact(model.add_new_contact())
    elif mode == 2:
        contact = model.get_search()
        phone_book = logger.get_phone_book()
        print(model.search_contact(phone_book, contact))
    elif mode == 0:
        print('Выход')
        break
    else:
        print('Такого режима нет')
