import string;

class Garden:
    def __init__(self, diagram, students=["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet",
                                          "Ileana", "Joseph", "Kincaid", "Larry"]):
        self._students = students
        students.sort()
        self._diagram = diagram.split("\n")
        self._plants = {"V": "Violets", "R": "Radishes", "G": "Grass", "C": "Clover"}

    def plants(self,child):
        childPo = self._students.index(child)
        childPl = [plant for line in self._diagram for plant in line[childPo*2:childPo*2 +2]]
        return [name for plant in childPl for key, name in self._plants.items() if plant is key]