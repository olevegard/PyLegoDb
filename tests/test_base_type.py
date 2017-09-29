from item_types.base_type import BaseType


def create_tuple_from_csv(csv_line: str):
    values = csv_line.split(",")
    return int(values[0]), values[1], values[2], values[3] == "True"


class TestBaseType:
    def test_that_we_can_get_tuple_from_generator(self):
        colors = [
            (0, "Black", "000000", False),
            (1, "Red", "FF0000", False),
            (2, "Green", "00FF00", False),
            (3, "Blue", "0000FF", False),
            (4, "White", "FFFFFF", False)
        ]

        BaseType.save_tuple_as_csv("tuple", colors)

        gen = BaseType.get_tuple_from_file_generator("tuple", create_tuple_from_csv)

        for tup in colors:
            assert next(gen) == tup
