from common.data import Data
from common.note import Note
from common.json_reader import JsonReader


class Run:

    def run(self):
        command = self.__read_command()
        if command == 1:
            self.__run_add_note()
        elif command == 2:
            self.__run_edit_note()
        elif command == 3:
            self.__run_read_note()
        elif command == 4:
            self.__run_delete_note()
        elif command == 5:
            self.__run_print_list_headers()
        elif command == 6:
            self.__run_print_all_notes()
        elif command == 7:
            self.__run_filter_by_date()

    def __run_add_note(self):
        data = Data()
        data.read_header()
        data.read_body()
        data.set_id_note()
        data.set_date()
        note = Note(data.get_args())
        note.add_note_to_json()
        print("\nЗаметка добавлена.")
        self.run()

    def __run_edit_note(self):
        data = Data()
        json_reader = JsonReader()
        data.read_id_note()
        if json_reader.check_id_note(data.get_id_note()):
            data.set_note()
            print(data)
            command = self.__read_command_for_edit()
            if command == 1:
                data.read_header()
                data.set_date()
                note = Note(data.get_args())
                note.edit_note_to_json()
                print("Заметка изменена.\n")
                self.run()
            elif command == 2:
                data.read_body()
                data.set_date()
                note = Note(data.get_args())
                note.edit_note_to_json()
                print("Заметка изменена.\n")
                self.run()
        else:
            print("Заметка не найдена.\n")
            self.run()

    def __run_read_note(self):
        data = Data()
        json_reader = JsonReader()
        data.read_id_note()
        if json_reader.check_id_note(data.get_id_note()):
            json_reader.print_note(data.get_id_note())
        else:
            print("Заметка не найдена.\n")
            self.run()
        self.run()

    def __run_delete_note(self):
        data = Data()
        json_reader = JsonReader()
        data.read_id_note()
        if json_reader.check_id_note(data.get_id_note()):
            data.set_note()
            note = Note(data.get_args())
            note.delete_note_to_json()
            print("Заметка удалена.\n")
        else:
            print("Заметка не найдена.\n")
            self.run()
        self.run()

    def __run_print_list_headers(self):
        json_reader = JsonReader()
        json_reader.print_list_headers()
        self.run()

    def __run_print_all_notes(self):
        json_reader = JsonReader()
        json_reader.print_all_notes()
        self.run()

    def __run_filter_by_date(self):
        json_reader = JsonReader()
        input_date_at = input("Введите начальную дата в формате гггг-мм-дд: ")
        input_date_to = input("Введите конечную дата в формате гггг-мм-дд: ")
        if json_reader.check_date(input_date_at, input_date_to):
            json_reader.print_notes_filtered_by_data(input_date_at,
                                                     input_date_to)
        else:
            print("Заметки не найдены\n")
        self.run()

    def __read_command(self):
        print("\nВведите номер команды.\n"
              "1. Добавить новую заметку\n"
              "2. Редактировать заметку\n"
              "3. Открыть заметку\n"
              "4. Удалить заметку\n"
              "5. Список заметок\n"
              "6. Вывести все заметки\n"
              "7. Выборка по дате\n"
              "8. Выход\n")
        try:
            command = int(input())
            if command < 1 or command > 8 or command is None:
                raise ValueError
            if command == 8:
                exit()
        except ValueError:
            print("Ошибка ввода. Повторите попытку.\n")
            self.run()
        else:
            return command

    def __read_command_for_edit(self):
        print("Введите номер команды.\n"
              "1. Редактировать заголовок\n"
              "2. Редактировать тело заметки\n"
              "3. Выход в главное меню\n")
        try:
            command = int(input())
            if command < 1 or command > 3 or command is None:
                raise ValueError
            if command == 3:
                self.run()
        except ValueError:
            print("Ошибка ввода. Повторите попытку.\n")
            self.run()
        else:
            return command
