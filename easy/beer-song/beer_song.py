def recite(start, take=1):
    wallBeers = []
    while take >= 1:
        s1 = "s" if start != 1 else ""
        s2 = "s" if start != 2 else ""
        num1 = start if start != 0 else "no more"
        num2 = "no more" if num1 == "no more" or num1 == 1 else num1 - 1
        down = "one" if num1 != 1 else "it"
        
        wallBeers.append("{} bottle{} of beer on the wall, {} bottle{} of beer.".format(num1,s1,num1,s1).capitalize())
        if num1 == "no more":
            wallBeers.append("Go to the store and buy some more, 99 bottles of beer on the wall.")
        else:
            wallBeers.append("Take {} down and pass it around, {} bottle{} of beer on the wall.".format(down,num2,s2))
        start = start - 1
        take = take - 1
        if take > 0:
            wallBeers.append("")
    return wallBeers
