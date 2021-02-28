class Allergies:
    def __init__(self, score):
        self.score = score
        self.vals = {1: "eggs",2:"peanuts",4:"shellfish",8:"strawberries",16:"tomatoes",32:"chocolate",64:"pollen",
                     128:"cats"}

    def allergic_to(self, item,score=None):
        scoring = score if score is not None else self.score
        if scoring < 1:
            return False
        for key,value in sorted(self.vals.items(),key = lambda x: x[0],reverse=True):
            if item == value and scoring >= key:
                return True
            elif scoring >= key:
                return self.allergic_to(item,scoring-key)

    @property
    def lst(self):
        if self.score < 1:
            return []
        
    def listicle(self,score=None,alls=[]):
        scoring = score if score is not None else self.score
        if self.score < 1:
            return []
        for key,value in sorted(self.vals.items(),key = lambda x: x[0],reverse=True):
            if scoring >= key:
                return self.listicle(scoring-key,alls+[value])