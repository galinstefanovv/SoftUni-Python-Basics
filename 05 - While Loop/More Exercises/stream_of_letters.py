import re
word = input()
pattern = re.compile("[A-Za-z]+")
sum = ""
c = False
o = False
n = False
while word != "End":

    if pattern.fullmatch(word) is not None:
        if word == "c":
            if c:
                sum += word
            c = True
        elif word == "o":
            if o:
                sum += word
            o = True
        elif word == "n":
            if n:
                sum += word
            n = True
        else:
            sum += word

        if c and o and n:
            print(sum, end=" ")
            sum = ""
            c = False
            o = False
            n = False
    word = input()