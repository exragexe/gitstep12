

class profesion:
    name_profesion = ""
    education = ""
    military_ticket = ""
    physical_form = ""
    price =""
    time_of_working = ""
    def __init__(self):
        print("Create object")
        self.name_profesion = "policeman"
        self.education = "law faculty at any university."
        self.military_ticket = "yes"
        self.physical_form = "midle"
        self.price = "500$"
        self.time_of_working = "a five-day working week with two days off"
    def ShowOn(self):
        print(f" Name profesion:{self.name_profesion}\n Level education:{self.education}\n Availability military ticket:{self.military_ticket}\n"
              f" Physical form:{self.physical_form}\n Price:{self.price}\n Time of working: {self.time_of_working}")
    def __del__(self):
        print("Delete object")
if __name__=="__main__":
    profesion = profesion()
    profesion.ShowOn()
    del profesion