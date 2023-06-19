from datetime import date
from datetime import datetime

from common.json_reader import JsonReader


class Data:

    def __init__(self):
        self.id_note = None
        self.header = None
        self.date = None
        self.body = None
        # self.header_for_find = None

    def __str__(self):
        return f'\nНомер: {self.id_note}\nЗаголовок: {self.header}\n' \
               f'Дата редактироания: {self.date}\nТело: {self.body}\n'

    # получение списка сущностей для инициализации экземпляра Note()
    def get_args(self):
        return [self.id_note, self.header, self.date, self.body]

    def get_id_note(self):
        return self.id_note

    # получение заметки по номеру для перезаписи или удаления
    def set_note(self):
        json_reader = JsonReader()
        objs = json_reader.read_json()
        for section in objs.values():
            for el in section:
                if self.id_note == el["id_note"]:
                    self.header = el["header"]
                    self.body = el["body"]
                    self.date = el["edit_date"]

    # генерация даты и времени из системы
    def set_date(self):
        current_date = date.today()
        current_time = datetime.now().time()
        current_time_f = f'{current_time.hour}:{current_time.minute}:' \
                         f'{current_time.second}'
        self.date = f'{current_date} {current_time_f}'

    #  генерация id для заметки (уникальное поле)
    def set_id_note(self):
        json_reader = JsonReader()
        objs = json_reader.read_json()
        if objs == {}:
            self.id_note = 1
        else:
            self.id_note = json_reader.get_all_id_note()[-1] + 1

    # считывание заголовка от пользователя
    def read_header(self):
        try:
            input_header = input("Введите заголовок: ")
            if input_header is None or input_header == "" or \
                    input_header.isspace():
                raise ValueError
        except ValueError:
            print("Заголовок не может быть пустым. Повторите попытку.")
            self.read_header()
        else:
            self.header = input_header

    # считывание намера заметки от пользователя
    def read_id_note(self):
        try:
            input_id_note = int(input("Введите номер заметки: "))
            if input_id_note is None or input_id_note == "":
                raise ValueError
        except ValueError:
            print("Неверный формат данных. Повторите попытку.")
            self.read_id_note()
        else:
            self.id_note = input_id_note

    # считывание тела от пользователя
    def read_body(self):
        self.body = input("Введите тело заметки: ")
