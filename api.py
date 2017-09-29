"""
Lego API

Used to run queries against Rebrickable and return results as JSON

TODO: Store data in csv files, add these to git. Test use temporary files so that the main ones don't change
"""
import requests


def build_url(query, params_string: str = None):
    if not params_string:
        return "https://rebrickable.com/api/v3/lego/{}?key=7f59c3197dac6633a3eb01c9688a3ea2".format(query)
    else:
        if params_string.startswith("?"):
            return "https://rebrickable.com/api/v3/lego/{}{}&key=7f59c3197dac6633a3eb01c9688a3ea2".format(
                query, params_string)
        elif params_string.startswith("&"):
            return "https://rebrickable.com/api/v3/lego/{}?key=7f59c3197dac6633a3eb01c9688a3ea2{}".format(
                query, params_string)
        else:
            return "https://rebrickable.com/api/v3/lego/{}?key=7f59c3197dac6633a3eb01c9688a3ea2&{}".format(
                query, params_string)


def do_lego_request(query, params_string: str = None):
    print("Request : " + str(build_url(query=query, params_string=params_string)))
    r = requests.get(url=build_url(query=query, params_string=params_string))
    return r.json()


def get_result_count(json_result):
    if "count" in json_result:
        return int(json_result["count"])
    else:
        return 1
