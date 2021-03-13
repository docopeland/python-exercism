def answer(question: str):
    quest = question[:-1].split()
    quest[:2]= []
    if len(quest) > 0 and quest[0].lstrip("-").isnumeric() and quest[-1].lstrip("-").isnumeric():
        val = int(quest[0])
    else:
        raise ValueError("bad question")
    if len(quest) > 1:
        for i in range(1,len(quest)-1):
            if quest[i].isnumeric():
                if quest[i+1].isnumeric() or quest[i-1].isnumeric():
                    raise ValueError("bad question")
                continue
            else:
                if quest[i] == "plus":
                    val = val + int(quest[i+1])
                if quest[i] == "minus":
                    val = val - int(quest[i+1])
                if quest[i] == "multiplied":
                    val = val * int(quest[i+2])
                if quest[i] == "divided":
                    val = val / int(quest[i+2])
                if quest[i] == "by":
                    continue
    return val