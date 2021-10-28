'''
路径要为全英文,图片名称也是
changeName 改成和文件夹一样前缀 + number +.jpg
convertToJPG
resizeImage 512*384

'''
import cv2
import matplotlib.pyplot as plt
import os
import re
import sys
from PIL import Image
import string
import numpy as np

PATH = r'C:\xunleixiazai\ferdb'


def resizeImage(file, NoResize):
    image = cv2.imread(file, cv2.IMREAD_COLOR)
    # print(type(image))

    # 如果type(image) == 'NoneType',会报错,导致程序中断,所以这里先跳过这些图片,
    # 并记录下来,结束程序后手动修改(删除)

    if image is None:
        NoResize += [str(file)]
    else:
        resizeImg = cv2.resize(image, (48, 48))
        cv2.imwrite(file, resizeImg)
        cv2.waitKey(100)


def resizeAll(root):
    # 待修改文件夹
    fileList = os.listdir(root)
    # 输出文件夹中包含的文件
    # print("修改前："+str(fileList))
    # 得到进程当前工作目录
    currentpath = os.getcwd()
    # 将当前工作目录修改为待修改文件夹的位置
    os.chdir(root)

    NoResize = []  # 记录没被修改的图片

    for file in fileList:  # 遍历文件夹中所有文件
        file = str(file)
        resizeImage(file, NoResize)

    print("---------------------------------------------------")

    os.chdir(currentpath)  # 改回程序运行前的工作目录

    sys.stdin.flush()  # 刷新

    if len(NoResize) != 0:
        print('没被修改的图片: ', root, '\t', NoResize)


def convertToJPG(dirName, childPATH):
    li = os.listdir(dirName)
    for filename in li:
        newname = filename
        newname = newname.split(".")
        if newname[-1] == "jpeg":
            newname[-1] = "jpg"
            newname = str.join(".", newname)
            filename = dirName + filename
            newname = dirName + newname
            os.rename(filename, newname)
        elif newname[-1] == 'png':
            newname[-1] = "jpg"
            newname = str.join(".", newname)
            filename = dirName + filename
            newname = dirName + newname
            os.rename(filename, newname)
        savePATH = childPATH + '/' + filename
        print(savePATH)
        # img = Image.open(savePATH).convert('RGB')
        # img.save(savePATH)

    print('convert To JPG is over!')
    print('Now resize images')


def renameall(root, NewFileName):
    # 待修改文件夹
    fileList = os.listdir(root)
    # 输出文件夹中包含的文件
    print("修改前：" + str(fileList))
    # 得到进程当前工作目录
    currentpath = os.getcwd()
    # 将当前工作目录修改为待修改文件夹的位置
    os.chdir(root)
    num = 1  # 名称变量

    for fileName in fileList:  # 遍历文件夹中所有文件

        preName, _ = fileName.split('_', 1)

        if preName != NewFileName:
            pat = ".+\.(jpg|png|pgm|jpeg|JPG)"  # 匹配文件名正则表达式
            pattern = re.findall(pat, fileName)  # 进行匹配
            os.rename(fileName, (str(NewFileName) + '_' + str(num) + '.' + pattern[0]))  # 文件重新命名
            num = num + 1  # 改变编号，继续下一项
    print("---------------------------------------------------")
    os.chdir(currentpath)  # 改回程序运行前的工作目录
    sys.stdin.flush()  # 刷新
    # print("修改后："+str(os.listdir(root)))       #输出修改后文件夹中包含的文件


# 两层文件夹
if __name__ == "__main__":
    # 含图片的文件夹叫做fileName,dir1的上层文件夹的路径为PATH
    for fileName in os.listdir(PATH):
        # 子文件夹路径
        dirName = PATH + '/' + fileName + '//'
        childPATH = PATH + '/' + fileName
        print(childPATH)
        renameall(childPATH, fileName)
        print(childPATH, 'rename is over')
        convertToJPG(dirName, fileName)
        print(childPATH, 'convertToJPG is over')
        resizeAll(childPATH)
        print(childPATH, 'resizeAll is over')
