import format as ft
from myprint import MPrint
import decorator as mdecorator
import numpy as np
import time, random

def textStrip(text, strips):
    if strips is not None:
        for i in strips:
            text=text.strip(i)
    return text

class DataMes():
    """About DataMes

    This class will receive a fileName and a strips list.
    The strips list is for strip unuseful character in the file.
    This class will analysis some sample statistics information and return structural data about file.

    Here they are:

    self.wordDict:
        return the dictionary which the key is word and the value is its frequency in the file.

    self.wordList:
        return the list which contains all the word unrepeatable.

    self.vacobsize:
        return the size of vocabulary text contains in this file.

    self.wordNum:
        return the number of words in this file.

    self.word2id
        return the dictionary which the key is word and the value is its id.
    self.word2idL:
        return the list which is the sort of self.word2id

    self.id2word
        return the dictionary which swap the key and value in self.word2id
    self.id2wordL:
        return the list which is the sort of self.id2word
    """

    def __init__(self, fileName, strips=['\n','.','',',']):
        self.wordNum = 0
        self.fileName = fileName
        self.lineNum = 0
        self.strips = strips
        # big data structure
        self.wordDict = dict()
        self.wordList = []
        self.wordIndex = {}
        self.wordIndexInverse = {}
        with open(self.fileName,'r') as f:
            for line in f:
                line = textStrip(line, self.strips)
                wordINLine = line.split()
                for word in wordINLine:
                    if word in self.wordDict:
                        self.wordDict[word] += 1
                    else:
                        self.wordDict.update({word:1})
                        self.wordList.append(word)
                self.wordNum += len(wordINLine)
                self.lineNum += 1
            for i in range(len(self.wordList)):
                self.wordIndex.update({self.wordList[i]:i})
                self.wordIndexInverse.update({i:self.wordList[i]})

    def wordRecord(self,outFileName):
        with open(outFileName,'w') as f:
            sortwordDict = ft.sortDict(self.wordDict, By="value")
            for i in sortwordDict:
                f.write(str(i[0])+' '+str(i[1])+'\n')

    def wordMesRecord(self,outFileName):
        with open(outFileName,'w' ,encoding="utf-8") as f:
            mes =  'Total number of words   : %d \n' % (self.wordNum)
            mes += 'Size of vocabulary      : %d \n' % (self.vocabSize)
            mes += 'Counts on lines         : %d \n' % (self.lineNum)
            f.write(mes)

    @property
    def vocabSize(self):
        return len(self.wordList)
    # 利用两个字典, wordIndex 和 wordIndexInverse 来进行 单词到数字的转化,用于其他数据结构的索引\
    @property
    def word2id(self):
        return self.wordIndex
    @property
    def word2idL(self):
        word2idlist = ft.sortDict(self.wordIndex, By="value")
        return word2idlist
    @property
    def id2word(self):
        return self.wordIndexInverse
    @property
    def id2wordL(self):
        id2wordlist = ft.sortDict(self.wordIndexInverse, By="key")
        return id2wordlist
    @property
    def wordProb(self, subsampling=True):
        wordProb = {}
        for word in self.wordList:
            z_w = self.wordDict[word]/self.wordNum
            if subsampling:
                prob = np.sqrt(z_w*1000+1)*0.001/z_w
            else:
                prob = z_w
            wordProb.update({word:prob})
        return wordProb

    def __help__():
        print("help message")

    # eliminate the words which frequency are less than threshold
    def filter(self,threshold):
        filterWords = []
        newwordList = []
        # print len(self.wordList)
        for i in range(len(self.wordList)):
            if self.wordDict[self.wordList[i]] <= threshold:
                filterWords.append(self.wordList[i])
                index = self.wordIndex[self.wordList[i]]
                del self.wordIndex[self.wordList[i]]
                del self.wordIndexInverse[index]
            else:
                newwordList.append(self.wordList[i])
        self.wordList = newwordList
        for word in filterWords:
            del self.wordDict[word]
            self.wordNum -= 1

    # return random word generator in form of iterator.
    def wordRandomIterator(self, size):
        id2word = self.id2word
        id2wordL = self.id2wordL
        wordProb = self.wordProb
        for i in range(size):
            while(True):
                indexProb = random.randint(0, self.vocabSize-1)
                useProb = random.random()
                word = id2word[indexProb]
                wordp = wordProb[word]
                if wordp < useProb:
                    break
            yield id2word[indexProb]

if __name__ == '__main__':
    a = DataMes("/home/dreamer/codes/learning_code/pytorch/lm/lstmLM/data/ptb.train.txt")
    # a.filter(3)
    mprint = MPrint("./logging.txt")
    adict = a.wordDict
    alist = a.wordList
    awordDict = a.wordDict
    aword2id = a.word2idL
    aid2word = a.id2wordL
    mprint.plist2f(aid2word,'aid2word')
    mprint.pdict2f(awordDict,"awordDict")
    for i in a.wordRandomIterator(10000):
        pass
