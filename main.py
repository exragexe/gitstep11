



import csv
import re
file_old = "ex3old.csv"
file_new = "ex3new.csv"

try:
    with open(file_old, "r") as csvold:
        allwords = csvold.readlines()
        onerow = re.split(",|\n|''", allwords[0])
        onerow1 = re.split(",|\n|''", allwords[2])
        onerow2 = re.split(",|\n|''", allwords[4])
        onerow3 = re.split(",|\n|''", allwords[6])
        onerow4 = re.split(",|\n|''", allwords[8])
        onerow5 = re.split(",|\n|''", allwords[10])
        data = [{onerow[0]: onerow1[0], onerow[1]: onerow1[1], onerow[2]: onerow1[2], onerow[3]: onerow1[3],
                 onerow[4]: onerow1[4]},
                {onerow[0]: onerow2[0], onerow[1]: onerow2[1], onerow[2]: onerow2[2], onerow[3]: onerow2[3],
                 onerow[4]: onerow2[4]},
                {onerow[0]: onerow3[0], onerow[1]: onerow3[1], onerow[2]: onerow3[2], onerow[3]: onerow3[3],
                 onerow[4]: onerow3[4]},
                {onerow[0]: onerow4[0], onerow[1]: onerow4[1], onerow[2]: onerow4[2], onerow[3]: onerow4[3],
                 onerow[4]: onerow4[4]},
                {onerow[0]: onerow5[0], onerow[1]: onerow5[1], onerow[2]: onerow5[2], onerow[3]: onerow5[3],
                 onerow[4]: onerow5[4]}
                ]
    with open(file_new, "w") as csvnew:
        writer = csv.DictWriter(csvnew, onerow)
        writer.writeheader()
        for i in data[::-1]:
            writer.writerow(i)

except IOError:
    print("io error")