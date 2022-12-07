

class phone:
    model = ""
    display = ""
    procesor = ""
    timeautoworking = ""
    size = ""
    camera = ""
    frontal_camera = ""
    price = ""
    def __init__(self):
        print("Create object")
        self.model = "Iphone 11(2019)"
        self.display = "Liquid Retina HD 6.1"
        self.procesor = "A13"
        self.timeautoworking = "many 17 hours"
        self.size = "150,9 х 75,7 х 8,3 мм"
        self.camera = "12Мп+12Мп"
        self.frontal_camera = "12Мп"
        self.price = "599+ $"
    def ShowOn(self):
        print(f" Model:{self.model}\n Display:{self.display}\n Procesor:{self.procesor}\n Time auto working:{self.timeautoworking}\n"
              f" Size:{self.size}\n Camera:{self.camera}\n Frontal camera:{self.frontal_camera}\n Price:{self.price}")
    def __del__(self):
        print("Delete object")
if __name__=="__main__":
    phone = phone()
    phone.ShowOn()
    del phone
