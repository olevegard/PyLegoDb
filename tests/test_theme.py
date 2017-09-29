# {'id': 1, 'parent_id': None, 'name': 'Technic'},

from item_types.theme_type import ThemeType


class TestSet:
    def test_that_we_can_create_color_tuple_from_json(self):
        tup = ThemeType.create_tuple_from_json({"id": 1, "parent_id": None, "name": "Technic"})
        assert tup.id == 1
        assert tup.parent_id is None
        assert tup.name == "Technic"

        tup = ThemeType.create_tuple_from_json({"id": 2, "parent_id": 1, "name": "Artic Technic"})
        assert tup.id == 2
        assert tup.parent_id == 1
        assert tup.name == "Artic Technic"
