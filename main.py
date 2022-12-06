

class poshtomat:
    color = ""
    number_model = 0
    weight = 0
    height = 0
    width = 0
    numbersofcell = 0
    def __init__(self):
        print("Create object")
        self.color="black"
        self.number_model = 5010
        self.weight = "500 kg"
        self.height = "2 m"
        self.width = "1 m"
        self.numbersofcell = 16
    def ShowOn(self):
        print(f" Color of poshtmat: {self.color}\n № model: {self.number_model}\n Weight: {self.weight}\n"
              f" Height: {self.height}\n Width: {self.width}\n Numbers of cell: {self.numbersofcell}")
    def __del__(self):
        print("Delete object")
if __name__ == "__main__":
    poshtomat = poshtomat()
    poshtomat.ShowOn()
    del poshtomat