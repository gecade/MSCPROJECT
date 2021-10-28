##深度学习过程中，需要制作训练集和验证集、测试集。
import os, random, shutil
def moveFile(fileDir):
        pathDir = os.listdir(fileDir)
        filenumber=len(pathDir)
        rate=0.2
        picknumber=int(filenumber*rate)
        sample = random.sample(pathDir, picknumber)
        print (sample)
        for name in sample:
                shutil.move(fileDir+name, tarDir+name)
        return

if __name__ == '__main__':
	fileDir = 'C:\\Learning resource\\MCS PROJECT\\data\\ferdb_train\\neutral\\'    #源图片文件夹路径
	tarDir = 'C:\\Learning resource\\MCS PROJECT\\data\\ferdb_test\\neutral\\'    #移动到新的文件夹路径
	moveFile(fileDir)
