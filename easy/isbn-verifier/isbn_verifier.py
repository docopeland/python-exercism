import re

def is_valid(isbn):
    isbn = isbn.replace("-","")
    letters = re.findall("[A-Z]",isbn)
    if (letters == [] or (letters == ["X"] and isbn.endswith("X"))) and len(isbn) == 10:
        mult = range(10,0,-1)
        if isbn.endswith("X"):
            isbn = isbn[:10]
            isbnList = [int(isbn[i]) for i in range(9)]
            isbnList.append(10)
        else:
            isbnList = [int(isbn[i]) for i in range(10)]
        isbnMult = [num1 * num2 for num1, num2 in zip(isbnList,mult)]
        isbnTot = 0
        for num in isbnMult:
            isbnTot = isbnTot + num
        return isbnTot % 11 == 0
    else:
        return False

