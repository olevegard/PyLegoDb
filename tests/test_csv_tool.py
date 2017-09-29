from item_types.color_type import Color, ColorType
from item_types.theme_type import Theme
from item_types.part_type import Part
from item_types.set_type import Set
import csv_tool




class TestCsvToool:
    def test_that_we_can_write_and_read(self):
        color = Color(id='0', name="Black", rgb="123456", is_trans='False')
        csv_tool.write_tuple_to_csv("tests/temp/tuptest.csv", color)

        color_2 = next(csv_tool.read_tuple_from_csv("tests/temp/tuptest.csv", ColorType.color_make))
        assert color == color_2

    def test_that_we_can_write_and_read(self):
        with open("tests/temp/tuptest.csv", "w") as f:
            f.write("0, Black, 123456, False")
        color = Color(id='0', name="Black", rgb="123456", is_trans='False')
        csv_tool.write_tuple_to_csv("tests/temp/tuptest.csv", color)

        color_2 = next(csv_tool.read_tuple_from_csv("tests/temp/tuptest.csv", ColorType.color_make))
        assert color == color_2
