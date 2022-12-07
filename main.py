

class musicinstrument:
    instrument = ""
    type = ""
    color = ""
    size = ""
    type_mechanics = ""
    weight = ""
    num_of_keys = 0
    polifoniya = 0
    def __init__(self):
        print("Create object")
        self.instrument = "pianino"
        self.type = "synthesizer"
        self.color = "black"
        self.size = "930 x 256 x 73 мм"
        self.weight = "3.3 kg"
        self.type_mechanics = "semi-weighted"
        self.num_of_keys = 61
        self.polifoniya = 48

    def ShowOn(self):
        print(f" Name of music instrument:{self.instrument}\n Type:{self.type}\n Color:{self.color}\n Size:{self.size}\n"
              f" Weight:{self.weight}\n Type of mechanics:{self.type_mechanics}\n Numbers of keys:{self.num_of_keys}\n"
              f" Polifoniya:{self.polifoniya}")
    def __del__(self):
        print("Delete object")
if __name__ == "__main__":
    musicinstrument = musicinstrument()
    musicinstrument.ShowOn()
    del musicinstrument