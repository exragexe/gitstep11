

import csv
import re

file_old = "old.csv"
file_new = "new.csv"
newletters = []
try:
    with open(file_old, "r") as csvold:
        allwords = str(csvold.read())
        oneword = re.split(",|\n|''",allwords)
        for word in oneword:
            if len(word) >= 7:
                newletters.append(word)
                newletters.append(",")
    with open(file_new, "w") as csvnew:
        csvnew.writelines(newletters)
except IOError:
    print("io error")