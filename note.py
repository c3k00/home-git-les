import json
import os
import subprocess
import datetime

def create_note():
    title = input("Введите заголовок заметки: ")
    text = input("Введите текст заметки: ")
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {"title": title, "text": text, "date": date}
    filename = note["title"] + ".json"
    with open(filename, "w") as file:
        json.dump(note, file)
    print(f"Заметка сохранена в файле {filename}")
    return note

# def save_note(note):
#     filename = note["title"] + ".json"
#     with open(filename, "w") as file:
#         json.dump(note, file)
#     print(f"Заметка сохранена в файле {filename}")


def show_notes():
    subprocess.call('clear' if os.name =='posix' else 'cls', shell=True)
    files = [f for f in os.listdir('.') if f.endswith(".json")]
    if files:
        print("Список заметок:")
        for filename in files:
            with open(filename) as file:
                note = json.load(file)
                print(f"Заголовок: {note['title']} >>> Дата создания: {note['date']}")
    else:
        print("Нет сохраненных заметок")

def date_note():
    subprocess.call('clear' if os.name =='posix' else 'cls', shell=True)
    files = [f for f in os.listdir('.') if f.endswith(".json")]
    if files:
        print("Список заметок:")
        for filename in files:
            with open(filename) as file:
                note = json.load(file)
                print(f"Дата: {note['date']} >>> Заголовок: {note['title']}")
    else:
        print("Нет сохраненных заметок")

def edit_note():
    show_notes()
    title = input("Введите заголовок заметки, которую хотите изменить: ")
    filename = title + ".json"
    if os.path.exists(filename):
        with open(filename) as file:
            note = json.load(file)
        print(f"Текущий текст заметки: {note['text']}")
        new_text = input("Введите новый текст заметки: ")
        # note["text"] = new_text
        new_date = note["date"]
        updated_note = {"title": title, "text": new_text, "date": new_date}
        with open(filename, "w") as file:
            json.dump(updated_note, file)
        print("Заметка изменена")
    else:
        print("Заметка с таким заголовком не найдена")

def delete_note():
    subprocess.call('clear' if os.name =='posix' else 'cls', shell=True)
    show_notes()
    title = input("Введите заголовок заметки, которую хотите удалить, либо нажмуте Enter для отмены: ")
    filename = title + ".json"
    if os.path.exists(filename):
        os.remove(filename)
        print("Заметка удалена")
    else:
        print("Заметка с таким заголовком не найдена")

def filter_by_date():
    date_note()
    date = input("Введите дату (гггг-мм-дд): ")
    files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith(".json")]
    notes_found = False
    for filename in files:
        with open(filename, "r") as file:
            note = json.load(file)
            if note["date"].split()[0] == date:
                if not notes_found:
                    print("Заметки, созданные", date + ":")
                    notes_found = True
                print("Заголовок:", note["title"])
                print("Текст:", note["text"])
                print("Дата создания:", note["date"])
                print("---------------------------")
    if not notes_found:
        print("Заметки, созданные", date + ", не найдены.")

def main():
    while True:
        # subprocess.call('clear' if os.name =='posix' else 'cls', shell=True)
        print(
            """
                       menu
            ____________________________
            |1. Создать заметку        |
            |2. Показать список заметок|
            |3. Изменить заметку       |
            |4. Удалить заметку        |
            |5. Делать выборку по дате |
            |6. Выйти из приложения    |
            ----------------------------
            """
        )
        choice = input("Выберите действие (1-6): ")
        
        if choice == "1":
            note = create_note()
        # elif choice == "2":
        #     if 'note' not in locals() or 'note' not in globals():
        #         print("Сначала создайте заметку")
        #         continue
        #     save_note(note)
        elif choice == "2":
            show_notes()
        elif choice == "3":
            edit_note()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            filter_by_date()
        elif choice == "6":
            break
        else:
            print("Неверный ввод, попробуйте еще раз")

if __name__ == "__main__":
    main()
