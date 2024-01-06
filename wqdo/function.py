from pathlib import Path
import cv2
import numpy as np
from scipy.signal import find_peaks
from pathlib import Path
import csv


def saveRGBtoCSV(rgb, numberNO: int, saveName: str):
    """saveName: path/name eg: wq/name or name"""
    savePath = Path.cwd()
    # open with newline="" avoids unnecessaty empty line
    with open(savePath.joinpath(saveName+".csv"), "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["R", "G", "B"])
        writer.writeheader()
        for r, g, b in rgb:
            writer.writerow({"R": r, "G": g, "B": b})


def readCSVcol(filePath: str, colName: str) -> list:
    """filePath like test.csv"""
    list = []
    with open(filePath) as file:
        reader = csv.DictReader(file)
        for row in reader:
            list.append(row[colName])
    return list


def getValueOfHeart(rgb):
    peak_Xtime, properties = find_peaks(rgb, height=5, distance=20)
    peak_Yval = rgb[peak_Xtime]
    len_X = len(rgb)
    len_Y = len(peak_Yval)
    heart = 30 * 60 * len_Y / len_X
    return heart


def getRawRGB(patientNum: int, dataDir: str):
    if not dataDir.endswith('/'):
        dataDir += '/'
    rawFile = Path.cwd().joinpath(dataDir+str(patientNum)+".mp4")
    rawVid = cv2.VideoCapture(rawFile.as_posix())
    vidLen = int(rawVid.get(cv2.CAP_PROP_FRAME_COUNT))
    rgbArray = np.zeros([vidLen, 3])
    print('processing ' + str(rawFile.name))
    count = 0
    success = 1
    while count < vidLen-1:
        success, image = rawVid.read()
        # process the image for R, G, B
        # the openCV package is using BGR protocol
        B2 = np.mean(image[:, :, 0])
        G1 = np.mean(image[:, :, 1])
        R0 = np.mean(image[:, :, 2])
        rgbArray[count] = [R0, G1, B2]
        count += 1
        count += 1
    return rgbArray


number = 3
videoPath = "data/raw-videos"
# rgbArray = getRawRGB(number, videoPath)
# saveRGB(rgbArray,3,"test3")

rgbArray = readCSVcol("test3.csv", "R")

rgbArray = np.array(rgbArray).astype(np.float32)

print(getValueOfHeart(rgbArray))
