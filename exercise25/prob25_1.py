import os
import csv
from functools import reduce

os.chdir(os.path.dirname(__file__))

listofnum = [["2", "4", "6"], ["3", "7", "5"], ["8", "9", "7"]]


def avg():
    with open("numbers.csv") as r,  open('numbers2.csv', 'w', newline='') as f:
        rows = csv.reader(r)
        for row in rows:
            new_list = [row[2].strip(), row[1].strip(), row[0].strip()]
            avglist = reduce(lambda a, b: a + b, map(int, new_list)) / len(new_list)
            new_list.append(avglist)
            print(new_list)

            w = csv.writer(f)
            w.writerows([new_list])

with open("numbers2.csv", "w", newline='') as f:
    w = csv.writer(f)
    w.writerows(listofnum)


if __name__ == "__main__":
    avg()






