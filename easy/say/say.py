def say(number,word=""):
    vals = {"1":"one","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight","9":"nine","0":""}
    tens = {"2":"twenty","3":"thirty","4":"forty","5":"fifty","6":"sixty","7":"seventy","8":"eighty","9":"ninty"}
    number = str(number)
    if len(number) > 12 or int(number) < 0:
        raise ValueError("Number is out of range")
    else:
        for i in range(len(number)-1,-1,-1):
            if number[i] == "0":
                continue
            if len(number[i:]) % 3 == 1:
                word = vals[number[i]] + word
            if len(number[i:]) % 3 == 2:
                if number[i] != 0 and number[i+1] == "0":
                    word = tens[number[i]] + "" + word
                else:
                    word = tens[number[i]] + "-" + word
            if len(number[i:]) % 3 == 0:
                word = vals[number[i]] + " hundred " + word
            if 
    return word