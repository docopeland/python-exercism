class Allergies:

    def __init__(self, score):
        self.score = score
        self.allergies = ["eggs","peanuts","shellfish","strawberries","tomatoes","chocolate","pollen","cats"]

    def allergic_to(self, item,score=None):
        return item in self.lst

    @property
    def lst(self):
        return [value for index,value in enumerate(self.allergies) if 2**index & self.score]