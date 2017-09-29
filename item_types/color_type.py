from collections import namedtuple
from .base_type import BaseType

Color = namedtuple("Color", ["id", "name", "rgb", "is_trans"])


def color_make(cls, iterable, new=tuple.__new__, len=len):
    if len(iterable) != 4:
        raise TypeError('Expected 4 arguments, got %d' % len(iterable))

    return Color(id=int(iterable[0]), name=iterable[1], rgb=iterable[2], is_trans=bool(iterable[3]))


Color._make = color_make
c = Color([1,2,3,4,5,6])

class ColorType(BaseType):
    @staticmethod
    def create_tuple_from_json(json_value: dict):
        return Color(
            id=int(json_value["id"]), name=json_value["name"],
            rgb=json_value["rgb"], is_trans=bool(json_value["is_trans"]))

    @staticmethod
    def create_tuple_from_csv(csv_line: str):
        values = csv_line.split(",")
        return Color(id=int(values[0]), name=values[1], rgb=values[2], is_trans=values[3] == "True")

    @staticmethod
    def get_tuple_as_dict(filename: str) -> dict:
        return BaseType.get_csv_file_as_dict(filename, create_from_csv_func=ColorType.create_tuple_from_csv)

    @staticmethod
    def get_as_dict(item : Color) -> dict:
        return { "id":item.id, "name":item.name, "rgb":item.rgb, "is_trans":item.is_trans}

    @staticmethod
    def color_make(iterable):
        if len(iterable) != 4:
            raise TypeError('Expected 4 arguments, got %d' % len(iterable))

        return Color(id=int(iterable[0]), name=iterable[1], rgb=iterable[2], is_trans=bool(iterable[3]))

