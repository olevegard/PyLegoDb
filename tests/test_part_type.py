from item_types.part_type import PartType, Part, BaseType

import api


class TestPartType:
    def test_that_we_can_create_tuple_from_json(self):
        tup = PartType.create_tuple_from_json({
            "part_num": "3001",
            "name": "Brick 2 x 4",
            "part_cat_id": 11,
            "part_url": "https://rebrickable.com/parts/3001/brick-2-x-4/",
            "part_img_url": "https://m.rebrickable.com/media/parts/elements/300126.jpg"
        })

        assert tup.id == '3001'
        assert tup.name == "Brick 2 x 4"
        assert tup.part_cat_id == 11
        assert tup.part_url == "https://rebrickable.com/parts/3001/brick-2-x-4/"
        assert tup.part_img_url == "https://m.rebrickable.com/media/parts/elements/300126.jpg"

    def test_that_we_can_get_line_from_generator(self):
        item_types = [
            Part(id="0", name="Black", part_cat_id=10, part_url="a", part_img_url="f"),
            Part(id="1", name="Red", part_cat_id=11, part_url="b", part_img_url="g"),
            Part(id="2", name="Green", part_cat_id=12, part_url="c", part_img_url="h"),
            Part(id="3", name="Blue", part_cat_id=13, part_url="d", part_img_url="i"),
            Part(id="4", name="White", part_cat_id=14, part_url="e", part_img_url="j")

        ]

        gen = PartType.tuple_list_to_string_generator(item_types)

        assert next(gen) == "0,Black,10,a,f"
        assert next(gen) == "1,Red,11,b,g"
        assert next(gen) == "2,Green,12,c,h"
        assert next(gen) == "3,Blue,13,d,i"
        assert next(gen) == "4,White,14,e,j"

    def test_that_we_can_get_line_of_tuple_values(self):
        store_color = Part(id=0, name="Black", part_cat_id=10, part_url="a", part_img_url="f")
        assert PartType.get_value_line_from_tuple(store_color) == "0,Black,10,a,f"

    def test_that_we_can_store_color_as_csv(self):
        item_types = [
            Part(id="0", name="Black", part_cat_id=10, part_url="a", part_img_url="f"),
            Part(id="1", name="Red", part_cat_id=11, part_url="b", part_img_url="g"),
            Part(id="2", name="Green", part_cat_id=12, part_url="c", part_img_url="h"),
            Part(id="3", name="Blue", part_cat_id=13, part_url="d", part_img_url="i"),
            Part(id="4", name="White", part_cat_id=14, part_url="e", part_img_url="j")
        ]

        PartType.save_tuple_as_csv("item_types", item_types)

        with open("item_types.csv", "r") as f:
            tuple_list = f.read().split("\n")

        assert tuple_list[0] == "0,Black,10,a,f"
        assert tuple_list[1] == "1,Red,11,b,g"
        assert tuple_list[2] == "2,Green,12,c,h"
        assert tuple_list[3] == "3,Blue,13,d,i"
        assert tuple_list[4] == "4,White,14,e,j"

    def test_that_we_can_get_tuple_from_generator(self):
        item_types = [
            Part(id="0", name="Black", part_cat_id=10, part_url="a", part_img_url="f"),
            Part(id="1", name="Red", part_cat_id=11, part_url="b", part_img_url="g"),
            Part(id="2", name="Green", part_cat_id=12, part_url="c", part_img_url="h"),
            Part(id="3", name="Blue", part_cat_id=13, part_url="d", part_img_url="i"),
            Part(id="4", name="White", part_cat_id=14, part_url="e", part_img_url="j")
        ]

        PartType.save_tuple_as_csv("item_types", item_types)

        gen = BaseType.get_tuple_from_file_generator("item_types", PartType.create_tuple_from_csv)

        for part in item_types:
            assert next(gen) == part

    def test_that_we_can_load_entire_tuple_as_dict(self):
        item_types = [
            Part(id="0", name="Black", part_cat_id=10, part_url="a", part_img_url="f"),
            Part(id="1", name="Red", part_cat_id=11, part_url="b", part_img_url="g"),
            Part(id="2", name="Green", part_cat_id=12, part_url="c", part_img_url="h"),
            Part(id="3", name="Blue", part_cat_id=13, part_url="d", part_img_url="i"),
            Part(id="4", name="White", part_cat_id=14, part_url="e", part_img_url="j")
        ]

        PartType.save_tuple_as_csv("test_parts", item_types)

        tuple_dict = PartType.get_tuple_as_dict("test_parts")

        for i in range(5):
            assert tuple_dict[str(i)] == item_types[i]

    def test_that_we_can_create_color_tuple_from_csv(self):
        tup = PartType.create_tuple_from_csv("1,Brick 2 x 4,11,aa,bb")

        assert tup.id == "1"
        assert tup.name == "Brick 2 x 4"
        assert tup.part_cat_id == 11
        assert tup.part_url == "aa"
        assert tup.part_img_url == "bb"

    def test_that_we_can_get_single_color_using_api(self):
        res = api.do_lego_request("parts/3001")
        assert res
        assert api.get_result_count(res) == 1

    def test_that_we_can_get_all_item_types_as_json(self):
        assert api.get_result_count(api.do_lego_request("parts")) >= 26938
