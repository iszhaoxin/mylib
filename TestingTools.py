import os,inspect
import re,time,random
import multiprocessing as mp
import matplotlib.pyplot as plt
# from decorator import *
import MyTools.decorator as decorator

def PrintLine(fileName):
    input_file = open(fileName,'r')
    while(1):
        for i in range(10):
            print input_file.readline()
        user_input = raw_input('Type stop to quit')
        if user_input == "stop":
            break

def draw(dataX,dataY):
    plt.plot(dataX, dataY)
    plt.show()

def MultiDraw(dataX,dataY):
    for data_x,data_y in zip(dataX,dataY):
        plt.plot(data_x, data_y)
    plt.show()

def plot(x,y,title,xlabel=None,ylabel=None,filepath = None,for_long = 0,show=0):
	plt.figure(figsize=(20,10))
	plt.title(title,size=35)
	plt.plot(x,y,'o')
	plt.xlabel(xlabel,size=35)
	plt.ylabel(ylabel,size=35)
	# plt.axis([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
	plt.plot(x,y,'g',label='data',linewidth=1,color = 'green')
	# plt.plot(x,y,'r')
	if filepath is not None:
		plt.savefig(filepath+title+'.png')
	if show==1:
		plt.show()

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
    # print wordDict
    printVar(word)
