from item_types.set_type import SetType


class TestSet:
    def test_that_we_can_create_color_tuple_from_json(self):
        set_json = {
            "set_num": "00-1", "name": "Weetabix Castle", "year": 1970, "theme_id": 414, "num_parts": 471,
            "set_img_url": "https://m.rebrickable.com/media/sets/00-1.jpg",
            "set_url": "https://rebrickable.com/sets/00-1/weetabix-castle/",
            "last_modified_dt": "2011-09-19T14:00:00Z"
        }

        tup = SetType.create_tuple_from_json(set_json)
        assert tup.id == "00-1"
        assert tup.name == "Weetabix Castle"
        assert tup.year == 1970
        assert tup.theme_id == 414
        assert tup.num_parts == 471
        assert tup.set_img_url == "https://m.rebrickable.com/media/sets/00-1.jpg"
        assert tup.set_url == "https://rebrickable.com/sets/00-1/weetabix-castle/"
