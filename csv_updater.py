"""
CSV Updater

Higher level functions for updating the CSV cache for all items
"""
import api
import os.path

from item_types.color_type import ColorType
from item_types.theme_type import ThemeType
from item_types.part_type import PartType
from item_types.base_type import BaseType
from item_types.set_type import SetType


def get_type_generator(query: str, do_request_func=api.do_lego_request):
    """
    Generator that yields parts as returned by /part/. Stops when it has returned all parts

    WARNING : Takes a long time to complete, only run if necessary

    :return: Each part as JSON
    """
    count = 1

    while True:
        part_list = do_request_func(query=query, params_string="?page=" + str(count))

        # Rest is now an array of parts
        for part_json in part_list["results"]:
            yield part_json

        # If next is None, we are on the last page and can break
        if not part_list["next"]:
            break

        if count == 3:
            break

        count += 1


def update_csv_file_for_type(item_type: str, json_to_tuple_converter):
    tuple_list = []

    for part_json in get_type_generator(query=item_type):
        tuple_list.append(json_to_tuple_converter(part_json))

    BaseType.save_tuple_as_csv(os.path.join("data_test", item_type + ".csv"), tuple_list)


def update_parts_csv_file():
    update_csv_file_for_type(item_type="parts", json_to_tuple_converter=PartType.create_tuple_from_json)


def update_sets_csv_file():
    update_csv_file_for_type(item_type="sets", json_to_tuple_converter=SetType.create_tuple_from_json)


def update_themes_csv_file():
    update_csv_file_for_type(item_type="themes", json_to_tuple_converter=ThemeType.create_tuple_from_json)


def update_colors_csv_file():
    update_csv_file_for_type(item_type="colors", json_to_tuple_converter=ColorType.create_tuple_from_json)


update_themes_csv_file()
update_sets_csv_file()
update_parts_csv_file()
update_colors_csv_file()
