def recite(start, take=1):
    wallBeers = []
    while take >= 1:
        s1 = "s" if start != 1 else ""
        s2 = "s" if start != 2 else ""
        num1 = start if start != 0 else "no more"
        if num1 == "no more":
            num2 = 99
        elif num1 == 1:
            num2 = "no more"
        else: num2 = num1 - 1
        down = "one" if num1 != 1 else "it"
        sen1 = "Take {} down and pass it around".format(down) if num1 != "no more" else "Go to the store and buy some more"
        wallBeers.append("{} bottle{} of beer on the wall, {} bottle{} of beer.".format(num1,s1,num1,s1).capitalize())
        wallBeers.append("{}, {} bottle{} of beer on the wall.".format(sen1,num2,s2))
        start = start - 1
        take = take - 1
        if take > 0:
            wallBeers.append("")
    return wallBeers
