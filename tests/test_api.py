import api


class TestHelper:
    def test_that_we_can_get_result_count(self):
        assert api.get_result_count({"test": "hello"}) == 1
        assert api.get_result_count({"count": "10"}) == 10

    def test_that_we_can_build_url(self):
        assert api.build_url("test") == "https://rebrickable.com/api/v3/lego/test?key=7f59c3197dac6633a3eb01c9688a3ea2"

    def test_that_we_can_build_url_with_params(self):
        assert api.build_url("test", "page=1") == \
               "https://rebrickable.com/api/v3/lego/test?key=7f59c3197dac6633a3eb01c9688a3ea2&page=1"

        assert api.build_url(
            "test", "?page=2") == "https://rebrickable.com/api/v3/lego/test?page=2&key=7f59c3197dac6633a3eb01c9688a3ea2"

        assert api.build_url(
            "test", "&page=3") == "https://rebrickable.com/api/v3/lego/test?key=7f59c3197dac6633a3eb01c9688a3ea2&page=3"

    def test_that_we_can_get_actual_results(self):
        res = api.do_lego_request("colors")
        assert api.get_result_count(res) >= 133

    def test_that_we_can_get_actual_results_for_pages(self):
        api.do_lego_request("colors", params_string="?page=1")
