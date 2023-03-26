import json
import os
import time

FILENAME = "notes.json"


def load_notes():
    if not os.path.exists(FILENAME):
        return {}
    with open(FILENAME, "r") as f:
        return json.load(f)


def save_notes(notes):
    with open(FILENAME, "w") as f:
        json.dump(notes, f, indent=4)


def add_note():
    notes = load_notes()
    note_id = input("Введите идентификатор заметки: ")
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    timestamp = int(time.time())
    note = {"id": note_id, "title": title, "body": body, "timestamp": timestamp}
    notes[note_id] = note
    save_notes(notes)
    print("Заметка добавлена.")


def edit_note():
    notes = load_notes()
    note_id = input("Введите идентификатор заметки: ")
    if note_id not in notes:
        print("Заметка не найдена.")
        return
    note = notes[note_id]
    title = input(f"Введите новый заголовок заметки (было '{note['title']}'): ")
    body = input(f"Введите новый текст заметки (было '{note['body']}'): ")
    timestamp = int(time.time())
    note["title"] = title
    note["body"] = body
    note["timestamp"] = timestamp
    save_notes(notes)
    print("Заметка изменена.")


def delete_note():
    notes = load_notes()
    note_id = input("Введите идентификатор заметки: ")
    if note_id not in notes:
        print("Заметка не найдена.")
        return
    del notes[note_id]
    save_notes(notes)
    print("Заметка удалена.")


def list_notes():
    notes = load_notes()
    if not notes:
        print("Список заметок пуст.")
        return
    for note_id, note in notes.items():
        print(f"{note['title']} ({note_id})")


def main():
    while True:
        print("Выберите действие:")
        print("1. Добавить заметку")
        print("2. Изменить заметку")
        print("3. Удалить заметку")
        print("4. Список заметок")
        print("5. Выход")
        choice = input("Введите номер действия: ")
        if choice == "1":
            add_note()
        elif choice == "2":
            edit_note()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            list_notes()
        elif choice == "5":
            break
        else:
            print("Некорректный номер действия.")


if __name__ == "__main__":
    main()