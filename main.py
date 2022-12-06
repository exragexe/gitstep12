

class privod:
    tipe_privod = "Rear"

class tormoz:
    tipe_tormoz = "Disc ventilated"

class engine:
    tipe_engine = "v12"
    size_engine = 2562
    klapansoncilindre_engine = 2
    power_engine = 150
    speed_enine = 6500, "in minutes"
    maxspeed_engine = 180

class transmision:
    tipe_transmission = "MKPP"
    numofsteps_transmision = 5

class dimensions:
    wheelbase_dimensions = 2600
    wheeltrackfront_dimensions = 1270
    rearwheeltrack_dimensions = 1250

class Car:
    marka = ""
    model = ""
    modification = ""
    massa = 0
    numofseats = 0
    def __init__(self):
        print("Create object")
        self.marka = "Ferrari"
        self.model = "Ferrari 212 Inter"
        self.modification = "Ferrari 212 Inter 2.6 150 л.с. 5МКПП 2.6 л. c 1951 по 1952"
        self.massa = 1000
        self.numofseats = 2
        self.privod = privod()
        self.tormoz = tormoz()
        self.engine = engine()
        self.transmision = transmision()
        self.dimensions = dimensions()

    def ShowOn(self):
        print(f" Marka: {self.marka}\n Model: {self.model}\n Modifications: {self.modification}\n Mass: {self.massa}\n"
              f" Numbers of seats: {self.numofseats}\n Drive unit: {self.privod.tipe_privod}\n Brakes: {self.tormoz.tipe_tormoz}\n"
              f" Engine: Size:{self.engine.size_engine}, Power:{self.engine.power_engine}, Tipe:{self.engine.tipe_engine}, "
              f"Klapans on cilindre:{self.engine.klapansoncilindre_engine}, Speed:{self.engine.speed_enine}, Max speed:{self.engine.maxspeed_engine}\n"
              f" Transmision: Tipe:{self.transmision.tipe_transmission}, Numbers of steps:{self.transmision.numofsteps_transmision}\n"
              f" Dimensions: Wheelbase:{self.dimensions.wheelbase_dimensions}, Wheel track front:{self.dimensions.wheeltrackfront_dimensions}, "
              f"Rear wheel track:{self.dimensions.rearwheeltrack_dimensions}")

    def __del__(self):
        print("Delete object")
if __name__ == "__main__":
    car = Car()
    car.ShowOn()
    del car