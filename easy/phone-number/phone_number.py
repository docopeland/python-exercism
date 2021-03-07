class PhoneNumber:
    def __init__(self, number):
        nons = ["0","1"]
        self.clean = "".join([num for num in number if num.isdigit()])
        self.squeaky = self.clean[1:] if len(self.clean) == 11 and self.clean[0] == "1" else self.clean
        if len(self.squeaky) != 10 or self.squeaky[0] in nons or self.squeaky[3] in nons:
            raise ValueError("Not valid phone number")

    @property
    def number(self):
        return self.squeaky

    def pretty(self):
        return "("+self.squeaky[0:3]+")-"+self.squeaky[3:6]+"-"+self.squeaky[6:]

    @property
    def area_code(self):
        return self.pretty()[1:4]


