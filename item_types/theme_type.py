from collections import namedtuple

Theme = namedtuple("Theme", ["id", "parent_id", "name"])


class ThemeType:
    @staticmethod
    def create_tuple_from_json(json_value: dict):
        return Theme(
            id=int(json_value["id"]),
            parent_id=json_value["parent_id"],
            name=json_value["name"]
        )
