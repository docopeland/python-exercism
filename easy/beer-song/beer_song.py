def recite(start, take=1):
    wallBeers = []
    while take >= 1:
        num = start
        bottles = "bottles"
        if start == 1:
            bottles = "bottle"
        if start == 0:
            num = "no more"
        wallBeers.append("{} {} of beer on the wall, {} {} of beer.".format(num,bottles,num,bottles).capitalize())
        if num == 2:
            bottles = "bottle"
        if num == "no more":
            wallBeers.append("Go to the store and buy some more, 99 bottles of beer on the wall.")
        if num == 1:
            wallBeers.append("Take it down and pass it around, no more bottles of beer on the wall.")
        if num != "no more" and start > 1:
            wallBeers.append("Take one down and pass it around, {} {} of beer on the wall.".format(start-1,bottles))
        start = start - 1
        take = take - 1
        if take > 0:
            wallBeers.append("")
    return wallBeers
