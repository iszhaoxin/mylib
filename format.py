 # -*- coding: UTF-8 -*-
import os,inspect
import re,time,random
import multiprocessing as mp
import matplotlib.pyplot as plt
# from decorator import *
import decorator as decorator

# chunk_size_line,divide bigfile into small chunks
def chunkify(fileName,lineCnt):
    fileSize = os.path.getsize(fileName)
    chunkRecord = []
    with open(file_name,'r') as f:
        chunkStart = f.tell()
        while(fileSize != chunkStart):
            for i in range(lineCnt):
                f.readline()
            chunkEnd = f.tell()
            yield chunkStart,chunkEnd-chunkStart
            chunkStart = chunkEnd

def read_in_chunks(fileName, chunk_size=1024):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    with open(file_name,'r') as file_object:
        while True:
            data = file_object.read(chunk_size)
            if not data:
                break
            yield data

def addToDict(word,wordDict,num=1):
    if word in wordDict:
        wordDict[word] += num
    else:
        wordDict.update({word:num})

def addToList(word,wordList):
    if word not in wordList:
        wordList.append(word)

def sortDict(dict, By="value", reverse=False):
    if By=="key":
        return sorted(dict.items(), key=lambda x:x[0], reverse=reverse)
    elif By=="value":
        return sorted(dict.items(), key=lambda x:x[1],reverse=reverse)

def sortTuple(Tuple):
    sortedList 	= sorted(Tuple.items(), key=lambda d: d[1], reverse=reverse)
    return sortedList

def mergeFile(files,c):
    cf = open(c,'wb')
    for file in files:
        a = open(file,'r')
        cf.write(a.read()+'\n')
        a.close()
    cf.close()

def textStrip(text, strips):
    if strips is not None:
        for i in strips:
            text=text.strip(i)
    return text

def lineCnt(filename):
    cnt = 0
    with open(filename,'r') as f:
        for line in f:
            cnt+=1
    return lines

def generateFileLists(filepath):
    fileLists 	= []
    files		= os.listdir(filepath)
    files.sort()
    for file in files:
        if os.path.isdir(filepath+file):
            fileLists.append(filepath+file+'/')
        else:
            fileLists.append(filepath+file)
    return fileLists

# 最后一步，截取多少行
def cutFile(filename, newfilename, rows):
    lines	   = content_lines(filename)
    newfile	 = open(newfilename,'wb')
    for n in range(rows+1):
        newfile.write(lines[n]+'\n')
    newfile.close()

def mkdir(filePathname):
    if os.path.exists(filePathname) == False:
        os.mkdir(filePathname)

def exists(filePathname):
    return os.path.exists(filePathname)

def generateFileLists(filepath):
    fileLists 	= []
    files		= os.listdir(filepath)
    for file in files:
        if os.path.isdir(filepath+file):
            fileLists.append(filepath+file+'/')
        else:
            fileLists.append(filepath+file)
    return fileLists

def mergeDirectory(path1,path2,path3):
    if os.path.exists(path3) == False:
        Tools.mkdir(path3)
    path1fileList = generateFileLists(path1)
    path2fileList = generateFileLists(path2)
    for file in path1fileList:
        shutil.copy(file[:-1], path3+file.split('/')[-1])
    for file in path2fileList:
        shutil.copy(file[:-1], path3+file.split('/')[-1])

def getdirsize(dir):
    size = 0
    for root, dirs, files in os.walk(dir):
       size += sum([os.path.getsize(os.path.join(root, name)) for name in files])
    return size

def select(word,path,aimPath):
    files = generateFileLists(path)
    newFile = open(aimPath+word+'.txt','wb')
    for file in files:
        paras = content_paras(file)
        for para in paras:
            content = para.split('::')[-1]
            iparas = content.split('\n')
            for ip in iparas:
                if re.search(word,ip):
                    newFile.write(ip)
                    newFile.write("\n")

if __name__ == '__main__':
    # @decorator.TimeRecorder
    # def function():
    #     time.sleep(2)
    #     print "I am a person"
    #
    # PrintLine('./glove.300d.txt')
    # # function()
    word = 'aa'
    # wordDict = {}
    # wordDict.update({'bb':1})
    # addToDict('bb',wordDict)
    # addToDict('aa',wordDict)
    print(wordDict)
    # printVar(word)
