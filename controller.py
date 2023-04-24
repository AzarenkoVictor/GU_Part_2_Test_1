from datetime import datetime
import view, database


def button_click():
    a = view.main_choise()
    print("")

    if a == 1:
        database.list()

    elif a == 2:
        print("Введите id заметки")
        id_found = int(input())
        database.note(id_found)

    elif a == 3:
        id = view.id_input()
        name = view.name_input()
        description = view.note_input()
        current_datetime = str(datetime.now())
        database.note_saving(id, name, description, current_datetime)

    elif a == 4:
        print("Введите id заметки")
        id_found = int(input())
        database.note_editing(id_found)

    elif a == 5:
        print("Введите id заметки")
        id_found = int(input())
        database.note_deleting(id_found)

    else:
        print("Введено некорректное значение (1-5)")
