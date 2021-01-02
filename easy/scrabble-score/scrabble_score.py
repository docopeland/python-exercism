values = {1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"], 2: ["D", "G"], 3: ["B", "C", "M", "P"],
          4: ["F", "H", "V", "W", "Y"], 5: ["K"], 8: ["J", "X"], 10: ["Q", "Z"]}

def score(word):
    scoring = [k for letter in list(word.upper()) for k,v in values.items() if letter in v]
    return sum(scoring)
