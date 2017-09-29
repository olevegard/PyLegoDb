from collections import namedtuple
from .base_type import BaseType

Part = namedtuple("Part", ["id", "name", "part_cat_id", "part_url", "part_img_url"])


class PartType(BaseType):
    @staticmethod
    def create_tuple_from_json(json_value: dict):
        return Part(
            id=json_value["part_num"], name=json_value["name"], part_cat_id=json_value["part_cat_id"],
            part_url=json_value["part_url"], part_img_url=json_value["part_img_url"])

    @staticmethod
    def create_tuple_from_csv(csv_line: str):
        values = csv_line.split(",")

        return Part(
            id=values[0], name=values[1], part_cat_id=int(values[2]),
            part_url=values[3], part_img_url=values[4].strip("\n"))

    @staticmethod
    def get_tuple_as_dict(filename: str) -> dict:
        return BaseType.get_csv_file_as_dict(filename, create_from_csv_func=PartType.create_tuple_from_csv)
