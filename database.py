from datetime import datetime
import json
import os.path


def list():
    if os.path.isfile("data.json"):
        with open("data.json", "r") as json_file:
            data = json.load(json_file)
            for item in data["note"]:
                print(item["id"], item["name"])
    else:
        print("Список заметок пуст !")
        return


def note(id: int):
    if os.path.isfile("data.json"):
        with open("data.json", "r") as json_file:
            data = json.load(json_file)
            for item in data["note"]:
                if item["id"] == id:
                    print(item["note"])
                    return
    else:
        print("Заметка отсутствует")
        return


def note_editing(id: int):
    if os.path.isfile("data.json"):
        with open("data.json") as json_file:
            data = json.load(json_file)
            print("Введите текст который будете редактировать ")
            field = str(input())
            print("Введите новый текст ")
            for item in data["note"]:
                if item["id"] == id:
                    if field == "id":
                        item[field] = int(input())
                    else:
                        item[field] = input()
                    break
        with open("data.json", "w") as json_file:
            json.dump(data, json_file)
    else:
        print("Заметка отсутствует")
        return


def note_saving(id: int, name: str, note: str, date: str):
    if os.path.isfile("data.json"):
        with open("data.json", "r") as json_file:
            data = json.load(json_file)
    else:
        data = {}
        data["note"] = []

    data["note"].append(
        {
            "id": id,
            "name": name,
            "note": note,
            "date": str(date),
        }
    )
    with open("data.json", "w") as outfile:
        json.dump(data, outfile)


def note_deleting(id: int):
    if os.path.isfile("data.json"):
        with open("data.json") as json_file:
            data = json.load(json_file)
            data["note"].pop(id - 1)
        with open("data.json", "w") as json_file:
            json.dump(data, json_file)


def date(x, format="%Y-%m-%d %H:%M"):
    return datetime.strptime(x.get("date"), format)
