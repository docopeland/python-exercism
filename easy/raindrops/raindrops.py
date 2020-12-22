def convert(number):
    rain = ((3,"Pling"),(5,"Plang"),(7,"Plong"))
    string = list()
    for k,v in rain:
        if number % k == 0:
            string.append(v)
    if string == list():
        return str(number)
    else:
        return "".join(map(str,string))
