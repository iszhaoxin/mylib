import time
import numpy as np
from dataset import DataMes
from myprint import MPrint
import random

class RandomGener:
    # dictFile should be a file with lots of plain text.
    # Here we use 100M plain text which used to train word2vec model
    def __init__(self, dictFile):
        self.datames = DataMes(dictFile)

    def textRandom2f(self, fileName, amount):
        mprint = MPrint(fileName)
        words = ''
        for word in self.datames.wordRandomIterator(amount):
            words = words + word + ' '
        wordl = mprint.pstr2f(words)

    def textRandom(self, amount):
        words = ''
        for word in self.datames.wordRandomIterator(amount):
            words = words + word + ' '
        return words

    def textRandomIterator(self, amount):
        # print 'baseamount2',self.baseamount
        return self.datames.wordRandomIterator(amount)

def numberRandom(amount, max='10000'):
    dataList = [random.randint(0,max) for i in range(amount)]
    return dataList

def numberRandom2f(amount, max='10000'):
    with open(fileName,'w', encoding='utf-8') as outFile:
        for i in range(amount):
            number = random.randint(0,max)
            outFile.write(str(number)+'\n')

def numberRandomIterator(amount, max='10000'):
    dataList = [random.randint(0,max) for i in range(amount)]
    for i in dataList:
        yield i


if __name__ == "__main__":
    a = RandomGener("/home/dreamer/codes/learning_code/pytorch/lm/lstmLM/data/ptb.train.txt")
    for i in a.numberRandomIterator(10):
        print(i)
    # print(a.textRandom('./test.txt', 10))
