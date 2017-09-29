from item_types.color_type import ColorType, Color, BaseType

import api


class TestColor:
    def test_that_we_can_get_full_tuple_string_array(self):

        colors = [
            Color(id=0, name="Black", rgb="000000", is_trans=False),
            Color(id=1, name="Red", rgb="FF0000", is_trans=False),
            Color(id=2, name="Green", rgb="00FF00", is_trans=False),
            Color(id=3, name="Blue", rgb="0000FF", is_trans=False),
            Color(id=4, name="White", rgb="FFFFFF", is_trans=False)
        ]
        tuple_list = ColorType.create_string_line_list(colors)
        assert tuple_list[0] == "0,Black,000000,False"
        assert tuple_list[1] == "1,Red,FF0000,False"
        assert tuple_list[2] == "2,Green,00FF00,False"
        assert tuple_list[3] == "3,Blue,0000FF,False"
        assert tuple_list[4] == "4,White,FFFFFF,False"

    def test_that_we_can_convert_to_dictionary(self):
        colors = [
            Color(id=0, name="Black", rgb="000000", is_trans=False),
            Color(id=1, name="Red", rgb="FF0000", is_trans=False),
            Color(id=2, name="Green", rgb="00FF00", is_trans=False),
            Color(id=3, name="Blue", rgb="0000FF", is_trans=False),
            Color(id=4, name="White", rgb="FFFFFF", is_trans=False)
        ]
        tuple_list = []
        for i in range(5):
            tuple_list.append(ColorType.get_as_dict(colors[i]))

        assert tuple_list[0] == { "id": 0, "name": "Black", "rgb": "000000", "is_trans": False}
        assert tuple_list[1] == { "id": 1, "name": "Red", "rgb": "FF0000", "is_trans": False}
        assert tuple_list[2] == { "id": 2, "name": "Green", "rgb": "00FF00", "is_trans": False}
        assert tuple_list[3] == { "id": 3, "name": "Blue", "rgb": "0000FF", "is_trans": False}
        assert tuple_list[4] == { "id": 4, "name": "White", "rgb": "FFFFFF", "is_trans": False}

    def test_that_we_can_convert_bac_and_forth(self):
        colors = [
            Color(id=0, name="Black", rgb="000000", is_trans=False),
            Color(id=1, name="Red", rgb="FF0000", is_trans=False),
            Color(id=2, name="Green", rgb="00FF00", is_trans=False),
            Color(id=3, name="Blue", rgb="0000FF", is_trans=False),
            Color(id=4, name="White", rgb="FFFFFF", is_trans=False)
        ]
        tuple_list = []
        for i in range(5):
            tuple_list.append(ColorType.get_as_dict(colors[i]))

        assert tuple_list[0] == { "id": 0, "name": "Black", "rgb": "000000", "is_trans": False}
        assert tuple_list[1] == { "id": 1, "name": "Red", "rgb": "FF0000", "is_trans": False}
        assert tuple_list[2] == { "id": 2, "name": "Green", "rgb": "00FF00", "is_trans": False}
        assert tuple_list[3] == { "id": 3, "name": "Blue", "rgb": "0000FF", "is_trans": False}
        assert tuple_list[4] == { "id": 4, "name": "White", "rgb": "FFFFFF", "is_trans": False}

        color_list = []

        for i in range(5):
            color_list.append(ColorType.get_tuple_as_dict(tuple_list[i]))

        assert color_list[0] == Color(id=0, name="Black", rgb="000000", is_trans=False)
        """
            Color(id=1, name="Red", rgb="FF0000", is_trans=False),
            Color(id=2, name="Green", rgb="00FF00", is_trans=False),
            Color(id=3, name="Blue", rgb="0000FF", is_trans=False),
            Color(id=4, name="White", rgb="FFFFFF", is_trans=False)
        """


    def test_that_we_can_get_line_from_generator(self):
        colors = [
            Color(id=0, name="Black", rgb="000000", is_trans=False),
            Color(id=1, name="Red", rgb="FF0000", is_trans=False),
            Color(id=2, name="Green", rgb="00FF00", is_trans=False),
            Color(id=3, name="Blue", rgb="0000FF", is_trans=False),
            Color(id=4, name="White", rgb="FFFFFF", is_trans=False)
        ]

        gen = ColorType.tuple_list_to_string_generator(colors)

        assert next(gen) == "0,Black,000000,False"
        assert next(gen) == "1,Red,FF0000,False"
        assert next(gen) == "2,Green,00FF00,False"
        assert next(gen) == "3,Blue,0000FF,False"
        assert next(gen) == "4,White,FFFFFF,False"

    def test_that_we_can_get_line_of_tuple_values(self):
        store_color = Color(id=1, name="Red", rgb="FF0000", is_trans=False)
        assert ColorType.get_value_line_from_tuple(store_color) == "1,Red,FF0000,False"

    def test_that_we_can_store_color_as_csv(self):
        colors = [
            Color(id=0, name="Black", rgb="000000", is_trans=False),
            Color(id=1, name="Red", rgb="FF0000", is_trans=False),
            Color(id=2, name="Green", rgb="00FF00", is_trans=False),
            Color(id=3, name="Blue", rgb="0000FF", is_trans=False),
            Color(id=4, name="White", rgb="FFFFFF", is_trans=False)
        ]

        ColorType.save_tuple_as_csv("colors", colors)

        with open("colors.csv", "r") as f:
            tuple_list = f.read().split("\n")
            assert tuple_list[0] == "0,Black,000000,False"
            assert tuple_list[1] == "1,Red,FF0000,False"
            assert tuple_list[2] == "2,Green,00FF00,False"
            assert tuple_list[3] == "3,Blue,0000FF,False"
            assert tuple_list[4] == "4,White,FFFFFF,False"

    def test_that_we_can_get_tuple_from_generator(self):
        colors = [
            Color(id=0, name="Black", rgb="000000", is_trans=False),
            Color(id=1, name="Red", rgb="FF0000", is_trans=False),
            Color(id=2, name="Green", rgb="00FF00", is_trans=False),
            Color(id=3, name="Blue", rgb="0000FF", is_trans=False),
            Color(id=4, name="White", rgb="FFFFFF", is_trans=False)
        ]

        ColorType.save_tuple_as_csv("colors", colors)

        gen = BaseType.get_tuple_from_file_generator("colors", ColorType.create_tuple_from_csv)

        for color in colors:
            assert next(gen) == color
    """
    def test_that_we_can_load_entire_tuple_as_dict(self):
        colors = [
            Color(id=0, name="Black", rgb="000000", is_trans=False),
            Color(id=1, name="Red", rgb="FF0000", is_trans=False),
            Color(id=2, name="Green", rgb="00FF00", is_trans=False),
            Color(id=3, name="Blue", rgb="0000FF", is_trans=False),
            Color(id=4, name="White", rgb="FFFFFF", is_trans=False)
        ]

        ColorType.save_tuple_as_csv("colors", colors)

        tuple_dict = ColorType.get_tuple_as_dict("colors")

        for i in range(5):
            assert tuple_dict[i] == colors[i]

    """
    def test_that_we_can_create_color_tuple_from_json(self):
        tup = ColorType.create_tuple_from_json({"id": 1007, "name": "Red", "rgb": "0xff0000", "is_trans": False})
        assert tup.id == 1007
        assert tup.name == "Red"
        assert tup.rgb == "0xff0000"
        assert not tup.is_trans

    def test_that_we_can_create_color_tuple_from_csv(self):
        tup = ColorType.create_tuple_from_csv("1007,Red,0xff0000,False")
        assert tup.id == 1007
        assert tup.name == "Red"
        assert tup.rgb == "0xff0000"
        assert not tup.is_trans

    def test_that_we_can_get_single_color_using_api(self):
        res = api.do_lego_request("colors/1007")
        assert res
        assert api.get_result_count(res) == 1

    def test_that_we_can_get_all_colors_as_json(self):
        assert api.get_result_count(api.do_lego_request("colors")) >= 133

    """
    def test_that_we_can_get_color_using_id(self):
        tup = api.get_color_single(1007)
        assert tup.id == 1007
        assert tup.name == "Reddish Lilac"
        assert tup.rgb == "8E5597"
        assert not tup.is_trans
    """
