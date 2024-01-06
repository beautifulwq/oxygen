import csv
import numpy as np
from numpy import polyfit


def readCSVcol(filePath: str, colName: str):
    list = []
    with open(filePath) as file:
        reader = csv.DictReader(file)
        for row in reader:
            list.append(row[colName])
    return list


def convertNPstrToNPfloat32(array: np.array):
    return array.astype(np.float32)


def linearRegression(numberNO: int):
    print("doing================", numberNO)
    # ppgValue = "data/ppg/Right/"+str(numberNO)+".csv"
    ppgValue = "data/ppg/Left/"+str(numberNO)+".csv"
    realOxy = "data/gt/"+str(numberNO)+".csv"
    frequence = 30

    oxyValue = readCSVcol(realOxy, "SpO2 1")
    greenValue = readCSVcol(ppgValue, "G")

    greenValue = np.array(greenValue)
    oxyValue = np.array(oxyValue)

    # resize greenValue to 30*N
    while greenValue.__len__() % frequence != 0:
        greenValue.resize(greenValue.__len__()-1)

    while greenValue.__len__() % oxyValue.__len__() != 0:
        oxyValue.resize(oxyValue.__len__()-1)

    greenValue = convertNPstrToNPfloat32(greenValue)
    # each 30 item get average
    greenValue = np.mean(greenValue.reshape(-1, frequence), axis=1)
    oxyValue = convertNPstrToNPfloat32(oxyValue)

    print("oxyValue ", oxyValue.__len__())
    print("greenValue ", greenValue.__len__())

    # if len not equal, select greenValue from end to begin with len of oxy
    if (oxyValue.__len__() < greenValue.__len__()):
        greenValue = greenValue[-oxyValue.__len__():]

    linearRegress = polyfit(greenValue, oxyValue, 1)
    return {linearRegress[0], linearRegress[1]}


if __name__ == "__main__":
    list = []
    for id in range(100001, 100007):
        list.append(linearRegression(id))
    print(*list, sep="\n")
