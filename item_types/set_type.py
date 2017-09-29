from collections import namedtuple

Set = namedtuple("Set", ["id", "name", "year", "theme_id", "num_parts", "set_img_url", "set_url"])


class SetType:
    @staticmethod
    def create_tuple_from_json(json_value: dict):
        return Set(
            id=json_value["set_num"], name=json_value["name"], year=int(json_value["year"]),
            theme_id=int(json_value["theme_id"]), num_parts=int(json_value["num_parts"]),
            set_img_url=json_value["set_img_url"], set_url=json_value["set_url"]
        )
