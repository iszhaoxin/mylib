import os

def sortDict(dict, By="value"):
    if By=="key":
        keys = dict.keys()
        keys.sort()
        return [[key,dict[key]] for key in keys]
    elif By=="value":
        return sorted(dict.items(), key=lambda x:x[1],reverse=True)

class MPrint:
    def __init__(self, fileName):
        self.file = open(fileName, 'w', encoding="utf-8")

    def plist2f(self, alist, name):
        assert(isinstance(alist, list))
        print("Length of {0} is {1}\n".format(name, len(alist)), file=self.file)
        print("[", end="\n", file=self.file)
        for i in alist:
            print("\t{0}\n".format(i),end="",file=self.file)
        print("]\n",end="",file=self.file)

    def plist(self, alist, name):
        assert(isinstance(alist, list))
        print("Length of {0} is {1}\n".format(name, len(alist)))
        print("[", end="\n")
        for i in alist:
            print("\t{0}\n".format(i))
        print("]\n")

    def pdict(self, adict, name, sort=False, by="value"):
        assert(isinstance(adict,dict))
        if by == "value" or by == "v" or by == "V" or by == "Value":
            sorted = sortDict(adict, By="value")
        elif by == "key" or by == "Key" or by == "K" or by == "k":
            sorted = sortDict(adict, By="key")
        else:
            raise Exception('Please input \"value\" or \"key\"')
        print("Length of {0} is {1}\n".format(name, len(sorted)))
        print("[", end="\n")
        for i in sorted:
            print("\t{0} :\t{1}".format(i[0], i[1]))
        print("]\n")

    def pdict2f(self, adict, name, sort=False, by="value"):
        assert(isinstance(adict,dict))
        if by == "value" or by == "v" or by == "V" or by == "Value":
            sorted = sortDict(adict, By="value")
        elif by == "key" or by == "Key" or by == "K" or by == "k":
            sorted = sortDict(adict, By="key")
        else:
            raise Exception('Please input \"value\" or \"key\"')
        print("Length of {0} is {1}\n".format(name, len(sorted)), file=self.file)
        print("[", end="\n", file=self.file)
        for i in sorted:
            print("\t{0} :\t{1}".format(i[0], i[1]), file=self.file)
        print("]\n", file=self.file)

    def pstr2f(self, astr, name):
        print("{0} is :\n".format(name), file=self.file)
        print(astr, end='\n', file=self.file)

if __name__ == "__main__":
    a = [1,1,2,3,4]
    # PrintList(a,'a')
