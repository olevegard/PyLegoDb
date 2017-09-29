from legodb import LegoDb


class TestLegoDb:
    def test_that_init_doesnt_download(self):
        # Make sure file is empty
        open("colors.csv", "w").close()

        lego_db = LegoDb()
        assert len(lego_db.colors) == 0

    def test_that_init_loads_from_file(self):
        with open("colors.csv", "w") as f:
            f.write("0,Black,000000,False\n")
            f.write("1,Red,FF0000,False\n")
            f.write("2,Green,00FF00,False\n")
            f.write("3,Blue,0000FF,False\n")
            f.write("4,White,FFFFFF,False\n")

        lego_db = LegoDb()
        assert len(lego_db.colors.keys()) == 5
