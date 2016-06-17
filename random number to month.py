import csv

with open('test.csv') as csvfile:
    readHere = csv.reader(csvfile, delimiter=",")
    num1 = input("Enter random number less than hundred   :   ")
    diff = []
    for row in readHere:
        diff.append(abs(int(num1) - int(row[3])))
    index = diff.index(min(diff))


with open('test.csv') as inf:
    readHereAgain = csv.reader(inf, delimiter=",")
    list =[]
    for asd in readHereAgain:
        list.append(asd[1])
    print(list[index])