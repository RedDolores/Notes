import json
import locale


class JsonReader:

    def __print_p(self, el):
        print('\nНомер: {}\nЗаголовок: {}\n'
              'Дата редактирования: {}\n' 'Тело: {}'
              .format(el["id_note"], el["header"],
                      el["edit_date"], el["body"]))

    # сортировка списка заметок по дате
    def __sort_dict_by_date(self):
        objs = self.read_json()
        if objs == {}:
            print("Файл пустой.")
        list_of_date = []
        for section in objs.values():
            for el in section:
                list_of_date.append(el["edit_date"])
        sorted(list_of_date)
        for index, el_l in enumerate(list_of_date):
            for section in objs.values():
                for el in section:
                    if el_l == el["edit_date"]:
                        list_of_date[index] = el
        objs["notes"] = list_of_date
        return objs

    # считывание файла, если его нет создается новый
    def read_json(self):
        try:
            with open('note.json') as f_n:
                return json.load(f_n)
        except FileNotFoundError:
            print("\nФайл не найден. Будет создан новый.\n")
            with open('note.json', 'w',
                      encoding=locale.getpreferredencoding()) as f_n:
                f_n.write('{}')
            with open('note.json') as f_nn:
                return json.load(f_nn)

    # список всех id для генератора id в Data
    def get_all_id_note(self):
        objs = self.read_json()
        list_of_id_note = []
        for section in objs.values():
            for el in section:
                list_of_id_note.append(el["id_note"])
        return sorted(list_of_id_note)

    # вывод заметки
    def print_note(self, id_note):
        objs = self.read_json()
        for section in objs.values():
            for el in section:
                if id_note == el["id_note"]:
                    self.__print_p(el)

    #  вывод из файла .json списка заголовков
    def print_list_headers(self):
        objs = self.__sort_dict_by_date()
        for section in objs.values():
            for el in section:
                print('\nНомер: {}\nЗаголовок: {}'.format(el["id_note"],
                                                          el["header"]))

    # вывод всех заметок на экран
    def print_all_notes(self):
        objs = self.__sort_dict_by_date()
        for section in objs.values():
            for el in section:
                self.__print_p(el)

    # выборка по дате
    def print_notes_filtered_by_data(self, date_at, date_to):
        objs = self.__sort_dict_by_date()
        for section in objs.values():
            for el in section:
                if date_at <= el["edit_date"].split(" ")[0] <= date_to:
                    self.__print_p(el)

    # проверка на вхождение номера заметки
    def check_id_note(self, id_note):
        objs = self.read_json()
        for section in objs.values():
            for el in section:
                if id_note == el["id_note"]:
                    return True

    # проверка на вхождение даты
    def check_date(self, date_at, date_to):
        list_of_date = []
        objs = self.__sort_dict_by_date()
        for section in objs.values():
            for el in section:
                list_of_date.append(el["edit_date"].split(" "))
        for i in range(len(list_of_date)):
            if date_at <= list_of_date[i][0] <= date_to:
                return True
