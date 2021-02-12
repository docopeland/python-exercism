def say(number,word=""):
    vals = {"1":"one","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight","9":"nine","0":""}
    tens = {"2":"twenty","3":"thirty","4":"forty","5":"fifty","6":"sixty","7":"seventy","8":"eighty","9":"ninty","0":""}
    teens = {"1":"eleven","2":"twelve","3":"thirteen","4":"fourteen","5":"fifteen","6":"sixteen","7":"seventeen",
             "8":"eighteen","9":"ninenteen"}
    number = str(number)
    if len(number) > 12 or int(number) < 0:
        raise ValueError("Number is out of range")
    elif number == "0":
        word = "zero"
    else:
        i = len(number) - 1
        while i > -1:
            if number[i] == "0":
                i = i - 1
                continue
            if len(number[i:]) == 4:
                word = " thousand " + word
            if len(number[i:]) == 7:
                word = " million " + word
            if len(number[i:]) == 10:
                word = " billion " + word
            if len(number[i:]) % 3 == 1:
                if i > 0 and number[i-1] == "1":
                    word = teens[number[i]] + word
                    i = i - 2
                else:
                    word = vals[number[i]] + word
            if len(number[i:]) % 3 == 2:
                if number[i] != "1" and number[i+1] == "0":
                    word = tens[number[i]] + "" + word
                else:
                    word = tens[number[i]] + "-" + word
            if len(number[i:]) % 3 == 0:
                word = vals[number[i]] + " hundred " + word
            i = i - 1
    return word.rstrip()