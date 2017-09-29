from item_types.color_type import ColorType

colors = {}


class LegoDb:
    def __init__(self):
        self.colors = ColorType.get_tuple_as_dict("colors")

    def init(self, download: bool):
        pass


"""
# print(json.dumps(api.do_lego_request("parts/3001"), indent=4))
from item_types.color_type import ColorType


print(str(ColorType.get_tuple_from_file_generator("colors.csv")))

t = ColorType()
print(str())


{i:i*2 for i in range(10)}

with open("colors.csv", "r") as f:
    for line in f:
        values = line.split(",")
        print("Values "+ str(values))
        clr = Color(id=int(values[0]), name=values[1], rgb=values[2], is_trans=values[3] == "True")
        print("Color : " + str(clr))
        :exception
    
"""
