class BaseType:
    @staticmethod
    def get_tuple_from_file_generator(filename, create_from_csv_func):
        filename = filename + (".csv" if not filename.endswith(".csv") else "")
        with open(filename, "r") as f:
            for line in f:
                yield create_from_csv_func(line)

    @staticmethod
    def get_csv_file_as_dict(filename, create_from_csv_func) -> dict:
        return {t.id: t for t in BaseType.get_tuple_from_file_generator(filename, create_from_csv_func)}

    @staticmethod
    def get_value_line_from_tuple(item_tuple):
        line = ""
        for val in item_tuple[:-1]:
            line += str(val) + ","
        return line + str(item_tuple[-1])

    @staticmethod
    def tuple_list_to_string_generator(tuple_list):
        for item_tuple in tuple_list:
            yield BaseType.get_value_line_from_tuple(item_tuple)

    @staticmethod
    def create_string_line_list(tuple_list):
        return list(BaseType.tuple_list_to_string_generator(tuple_list=tuple_list))

    @staticmethod
    def save_tuple_as_csv(filename: str, tuple_list):
        filename = filename + (".csv" if not filename.endswith(".csv") else "")
        with open(filename, "w") as f:
            for line in BaseType.tuple_list_to_string_generator(tuple_list=tuple_list):
                f.write(line + "\n")
