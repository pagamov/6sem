# https://www.blindtextgenerator.com/lorem-ipsum
from fuzzywuzzy import fuzz
import random
import string
from time import time
import matplotlib.pyplot as plt

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def GetText(path):
    f = open(path, "r")
    one = ''
    for word in f.read().split():
        ptr = ''
        for char in word:
            if char not in ['.',',','/',';',':','(',')','?','!']:
                ptr += char
        one += ' ' + ptr
    f.close()
    return one.lower()
def compare(t1,t2,size=10**10):
    t1 = t1[:min(size,min(len(t1),len(t2)))]
    t2 = t2[:min(size,min(len(t1),len(t2)))]
    return fuzz.WRatio(t1, t2) , min(size,min(len(t1),len(t2)))
def makeRandomText(size):
    res = ''
    for i in range(size):
        res += random.choice(string.ascii_letters)
        if random.random() < 0.2:
            res += ' '
    return res.lower()
def makeRandomWordText(paths,size):
    preres = []
    for path in paths:
        f = open(path, 'r')
        for word in f.read().split():
            ptr = ''
            for char in word:
                if char not in ['.',',','/',';',':','(',')','?','!']:
                    ptr += char
            preres.append(ptr.lower())
        f.close()
    res = random.choice(preres)
    while len(res) < size:
        res += ' ' + random.choice(preres)
    return res

print('\n\n\n'+bcolors.FAIL+'new run'+bcolors.ENDC)
# test 1
# text vs text
test1_data = [['text/cicero','text/farfaraway'],['text/cicero','text/kafka'],['text/farfaraway','text/kafka']]
print(bcolors.FAIL+'text vs text'+bcolors.ENDC)
def test1(paths):
    x,y = [],[]
    for test in range(len(paths)):
        x.append([])
        y.append([])
        t = time()
        t1,t2 = GetText(paths[test][0]),GetText(paths[test][1])
        for i in range(5,min(len(t1),len(t2)),25):
            x[test].append(i)
            y[test].append(compare(t1,t2,i)[0])
        print(paths[test][0],paths[test][1], end=' : ')
        print(round(time() - t,4), end=' sec with ')
        print(bcolors.OKGREEN+str(compare(t1,t2))+bcolors.ENDC)
        plt.plot(x[test], y[test],label=paths[test][0]+' vs '+paths[test][1])
    plt.xlabel('num of chars')
    plt.ylabel('percent of compare')
    plt.title('text vs text')
    plt.legend()
    plt.show()
# test1(test1_data)


# test 2
# text vs random letter text
test2_data = ['text/cicero','text/farfaraway','text/kafka']
print(bcolors.FAIL+'text vs random letter text'+bcolors.ENDC)
def test2(paths):
    x,y = [],[]
    for test in range(len(paths)):
        x.append([])
        y.append([])
        t = time()
        t1 = GetText(paths[test])
        for i in range(5,len(t1),25):
            t2 = makeRandomText(len(t1))
            x[test].append(i)
            y[test].append(compare(t1,t2,i)[0])
        print(paths[test], end=' : ')
        print(round(time() - t,4), end=' sec with ')
        print(bcolors.OKGREEN+str(compare(t1,t2))+bcolors.ENDC)
        plt.plot(x[test], y[test],label=paths[test]+' vs random letter')
    plt.xlabel('num of chars')
    plt.ylabel('percent of compare')
    plt.title('text vs random letter text')
    plt.legend()
    plt.show()
test2(test2_data)


# test 3
# text vs random word text
test3_data = ['text/cicero','text/farfaraway','text/kafka']
print(bcolors.FAIL+'text vs random word text'+bcolors.ENDC)
def test3(paths):
    x,y = [],[]
    for test in range(len(paths)):
        x.append([])
        y.append([])
        t = time()
        t1 = GetText(paths[test])
        for i in range(5,len(t1),25):
            t2 = makeRandomWordText(test3_data,len(t1))
            x[test].append(i)
            y[test].append(compare(t1,t2,i)[0])
        print(paths[test], end=' : ')
        print(round(time() - t,4), end=' sec with ')
        print(bcolors.OKGREEN+str(compare(t1,t2))+bcolors.ENDC)
        plt.plot(x[test], y[test],label=paths[test]+' vs random word')
    plt.xlabel('num of chars')
    plt.ylabel('percent of compare')
    plt.title('text vs random word text')
    plt.legend()
    plt.show()
test3(test3_data)


# test 4
# random letter text vs random letter text
print(bcolors.FAIL+'random letter text vs random letter text'+bcolors.ENDC)
def test4(num=10, size=1000):
    x,y = [],[]
    for test in range(num):
        x.append([])
        y.append([])
        t = time()
        t1,t2 = makeRandomText(size),makeRandomText(size)
        for i in range(5,len(t1),25):
            x[test].append(i)
            y[test].append(compare(t1,t2,i)[0])
        print(test, end=' : ')
        print(round(time() - t,4), end=' sec with ')
        print(bcolors.OKGREEN+str(compare(t1,t2))+bcolors.ENDC)
        plt.plot(x[test], y[test],label=str(test)+' random letter text')
    plt.xlabel('num of chars')
    plt.ylabel('percent of compare')
    plt.title('random letter text vs random letter text')
    plt.legend()
    plt.show()
test4(5, 8000)


# test 5
# random word text vs random word text
test5_data = ['text/cicero','text/farfaraway','text/kafka']
print(bcolors.FAIL+'random word text vs random word text'+bcolors.ENDC)
def test5(paths, num=10, size=1000):
    x,y = [],[]
    for test in range(num):
        x.append([])
        y.append([])
        t = time()
        t1,t2 = makeRandomWordText(paths,size),makeRandomWordText(paths,size)
        for i in range(5,len(t1),25):
            x[test].append(i)
            y[test].append(compare(t1,t2,i)[0])
        print(test, end=' : ')
        print(round(time() - t,4), end=' sec with ')
        print(bcolors.OKGREEN+str(compare(t1,t2))+bcolors.ENDC)
        plt.plot(x[test], y[test],label=str(test)+' random word text')
    plt.xlabel('num of chars')
    plt.ylabel('percent of compare')
    plt.title('random letter text vs random letter text')
    plt.legend()
    plt.show()
test5(test5_data, 5, 8000)
