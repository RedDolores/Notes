import json
import locale

from common.json_reader import JsonReader


class Note:

    # инициализация сущностей из экземпляра Data
    def __init__(self, *args):
        self.id_note = args[0][0]
        self.header = args[0][1]
        self.date = args[0][2]
        self.body = args[0][3]
        self.NOTE_DICT = {
            'id_note': int(self.id_note),
            'header': self.header,
            'edit_date': self.date,
            'body': self.body,
        }
        self.NOTES_DICT = {'notes': [self.NOTE_DICT]}
        self.local_coding = locale.getpreferredencoding()

    #  добавление новой заметки в .json файл
    def add_note_to_json(self):
        json_reader = JsonReader()
        objs = json_reader.read_json()
        if objs == {}:  # проверяем, если файл пустой (т.е. только {})
            with open('note.json', 'w', encoding=self.local_coding) as j_file:
                json.dump(self.NOTES_DICT, j_file, indent=4,
                          ensure_ascii=False)
        else:
            for el in objs.values():
                el.append(self.NOTE_DICT)
            with open('note.json', 'w', encoding=self.local_coding) as j_file:
                json.dump(objs, j_file, indent=4, ensure_ascii=False)

    # изменение существующей заметки
    def edit_note_to_json(self):
        json_reader = JsonReader()
        objs = json_reader.read_json()
        for section in objs.values():
            for el in section:
                if el["id_note"] == self.id_note:
                    el.update(self.NOTE_DICT)
        with open('note.json', 'w', encoding=self.local_coding) as j_file:
            json.dump(objs, j_file, indent=4, ensure_ascii=False)

    # удаление существующей заметки
    def delete_note_to_json(self):
        json_reader = JsonReader()
        objs = json_reader.read_json()
        for section in objs.values():
            for i in range(len(section)):
                if section[i]["id_note"] == self.id_note:
                    del section[i]
                    break
        with open('note.json', 'w', encoding=self.local_coding) as j_file:
            json.dump(objs, j_file, indent=4, ensure_ascii=False)
