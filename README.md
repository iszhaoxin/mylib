texthelper

### dataset.py

Contains "DataMes" class, here is concrete information:
About DataMes

- This class will receive a fileName and a strips list.The strips list is for strip unuseful character in the file. This class will analysis some sample statistics information and return structural data about file.

Here they are:

- self.wordDict:
    return the dictionary which the key is word and the value is its frequency in the file.

- self.wordList:
    return the list which contains all the word unrepeatable.

- self.vacobsize:
    return the size of vocabulary text contains in this file.

- self.wordNum:
    return the number of words in this file.

- self.word2id
    return the dictionary which the key is word and the value is its id.
- self.word2idL:
    return the list which is the sort of self.word2id

- self.id2word
    return the dictionary which swap the key and value in self.word2id
- self.id2wordL:
    return the list which is the sort of self.id2word

- Except for these, you can set the threshold to eliminate low frequency words with self.filter.And can't use self.wordRandomIterator to return random word generator in form of iterator.
"""

### generator.py
Contains "RandomGener" class, here is concrete information:
About RandomGener

- This class will receive a file which expected to be a large size of plain text.In func<__init__ > DataMes in dataset.py will be used to get the information and structural data of this file. Then, there accomplished several function based on DataMes.wordRandomIterator. Here is the concrete introduction.

- self.textRandom2f(fileName, amount):
    fileName is the out file's name and amount represent how many words you want to generate. Finally print it to file.

- self.textRandom(amount):
    It's same as textRandom2f but doesn't print it to file, just return a str.

- self.textRandomIterator(amount):
    It's same as textRandom2f but doesn't print it to file, just return a iterator.


### myprint.py
Contains "MPrint" class, here is concrete information:
About MPrint

- This class will receive a file's name which supposed to be the output stream when output to file.
Here has accomplished the Implementation of three kinds of data structure - <list dict and str>

- def plist2f(self, alist, name):
    alist : input list
    name  : the name of this list
    Print to file
- def plist(self, alist, name):
    alist : input list
    name  : the name of this list
    Print to screen
- def pdict(self, adict, name, sort=False, by="value"):
    pdict : input dict
    name : name of this dict
    sort : Beacuse I need to turn the dict to list, so it can be select whether sort it.
    By : sort by "value" of by "key"
- def pdict2f(self, adict, name, sort=False, by="value"):
    print to file
- def pstr2f(self, astr):
    print str to file.
