import os
from pathlib import Path
import os
import scipy
from scipy.signal import savgol_filter
import cv2 as cv
import numpy as np
from scipy.signal import find_peaks
from matplotlib import pyplot as plt
from pathlib import Path
import scipy.signal as signal


def findFile(path, num, type):
    fileList = list(Path(path).rglob('*' + type))
    # print(fileList)
    file = None
    for f in fileList:
        if str(num) in f.name:
            file = f
            # print(file)
            print('analizing:       '+(f.name)+"    in    "+str(path))
        else:  # couldn't find the file
            pass
    return file


def writeGvalue(words, number):
    try:
        dir = os.makedirs('values',)
        file = open('values\\%d' % (number)+'.txt', 'a+', encoding='utf-8')
        file.write(str(words))
        print('write %d success' % number)
        file.close()
    except:
        file = open('values\\%d' % (number)+'.txt', 'a+', encoding='utf-8')
        file.write(str(words))
        print('write %d success' % number)

        file.close()


def readGvalue(number):
    try:
        number = str(number)
        filpath = findFile('values', number, '.txt')
        thisfile = open(filpath, 'r', encoding='utf-8')
        print('open %s ' % number)
        array = ''
        while True:
            temparray = thisfile.readline()
            temparray = temparray.strip("\n")
            if temparray == "":
                break
            array += temparray
        array = array.strip('[')
        array = array.strip(']')

        # print(array)
        array = array.split(' ')
        # list类型的array（已经过滤空串）
        array = list(filter(lambda cx: cx != '', array))
        thisfile.close()
        return array
    except Exception as err:
        print('读取文件失败,错误原因如下')
        print(err)


def getvalueofheart(rgb):
    peaks, properties = find_peaks(rgb, height=5, distance=20)
    # 这个是关键find_reaks，可以选合适的峰值，如果不滤波可能通过调好参数来选出合适的峰值
    peaksyval = rgb[peaks]
    xtolen = len(rgb)
    ytolen = len(peaksyval)
    # print(30 * 60 * ytolen / xtolen)
    heart = 30 * 60 * ytolen / xtolen
    return heart


def getRawofRGB(patientNum, dataDir, sel):
    # sel=0,blue,sel=1;green,sel=2,red
    rawFile = findFile(dataDir, patientNum, '.mp4')
    rawVid = cv.VideoCapture(rawFile.as_posix())
    vidLen = int(rawVid.get(cv.CAP_PROP_FRAME_COUNT))
    print('videolength:    ', vidLen, 'frame')
    rgbArray = np.zeros(vidLen)  # vidLen行，1列
    print('processing:      ' + str(rawFile.name))
    print('please wait...')
    count = 0
    success = 1
    while count < vidLen-1:
        success, image = rawVid.read()
        # process the image for R, G, B
        # the openCV package is using BGR protocol
        G1 = np.mean(image[:, :, sel])
        G1 = format(G1, '.8f')  # 控制小数位数
        rgbArray[count] = G1
        count += 1
    # print(rgbArray)
    return rgbArray


# videofile_path=str(Path.cwd())+'/videofile'
# for i in os.listdir(videofile_path):
#     rgbto_ana=getRawofRGB(i,videofile_path,1)
#     writeGvalue(rgbto_ana,1)
reading = readGvalue(1)
for i in reading:
    print(i)
