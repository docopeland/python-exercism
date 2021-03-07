class PhoneNumber:
    def __init__(self, number):
        nons = ["0","1"]
        self.clean = "".join([num for num in number if num.isdigit()])
        self.number = self.clean[1:] if len(self.clean) == 11 and self.clean[0] == "1" else self.clean
        if len(self.number) != 10 or self.number[0] in nons or self.number[3] in nons:
            raise ValueError("Not valid phone number")
        self.area_code = self.pretty()[1:4]

    def pretty(self):
        return "({})-{}-{}".format(self.number[0:3], self.number[3:6], self.number[6:])