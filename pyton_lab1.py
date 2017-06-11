# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random, os, os.path, math

#rand = random.randint(1,10)
"""
Zadanie 1
print("Hello World")

#Zadanie 2
name = input("Podaj imie: ")
surname = input("Podaj nazwisko: ")
date = input("Podaj date urodzenia: ")
print(name, surname, date)

#Zadanie 3
print (len([name for name in os.listdir('.') if os.path.isfile(name)]))

#Zadanie 4
class Locker:
    def __init__(self, password):
        self.p = password
    
    def checkPass(self, password):
        if self.p == password:
            print("Password valid")
        else:
            print("Password invalid")

p = input("Wprowadz haslo: ")
locker = Locker(p)
p = input("Sprawdz haslo: ")
locker.checkPass(p)

#Zadanie 5
def files(directory, dcr=""):
    for f in os.listdir(directory):
        if os.path.isdir(f):
            print(f+":")
            files(directory + "/" + f, dcr+"--")
        else:
            print(dcr + f)
    
files(".")

#Zadanie 6
d = "./img"
for f in os.listdir(d):
    base = os.path.splitext(d+"/"+f)[0]
    os.rename(d+"/"+f, base + ".png")

#Zadanie 7
class Equation:
    roots = []
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def calcRoots(self):
        #y = a*x^2 + bx + c
        if self.a == 0:
           return self.b
            
        delta = (self.b**2)-4*self.a*self.c       
        if delta > 0:        
            x1 = (-self.b - math.sqrt(delta)) / (2*self.a)
            x2 = (-self.b + math.sqrt(delta)) / (2*self.a)
            roots = [x1, x2]
        elif delta == 0:
            x = -self.b/(2*self.a)
            roots = x
        else:
            absdelta = math.fabs(delta)
            
            print(absdelta) 
            temp1 = str(-self.b/(2*self.a))
            x1 = x2 = temp1            
            temp2 = math.sqrt(absdelta)/(2*self.a)
            
            if temp2 > 0:
                x1 += " - "
                x2 += " + "
            else:
                x1 += " - "
                x2 += " + "
                
            x1 += str(temp2)+"i"            
            x2 += str(temp2)+"i" 
            roots = [x1, x2]
            
        return roots
            
equation = Equation(4,5,1)
r = equation.calcRoots()
print(r)

#Zadanie 8
class Numbers:
    def __init__(self, arr):
        self.data = arr

    def orderDesc(self):
        self.dataDesc = self.data
        
        for i in range(len(self.dataDesc)):
            for j in range(len(self.dataDesc)-1):
                if (self.dataDesc[j] < self.dataDesc[j+1]):
                    self.dataDesc[j], self.dataDesc[j+1] = self.dataDesc[j+1], self.dataDesc[j]
        return self.dataDesc
    
    def validateSort(self):
        tmpData = self.data
        tmpData.sort(reverse=False)
        if tmpData == self.dataDesc:
            print("Given array is correctly sorted descending")
  
numbers = Numbers(random.sample(range(1,100), 50))
print(numbers.data)
print(numbers.orderDesc())
numbers.validateSort()

#Zadanie 9
toRemove = ["is", "the", "and", "never", "why"]
f = open("C:/Users/Darek/.spyder-py3/sport/Sebastian Vettel.txt", "r")
content = f.read()
f.close()
newcontent = [content.replace(word, "") for word in toRemove]
print(newcontent)

#Zadanie 10
d = dict({"is":"the", "the":"it", "and":"almost", "never":"why"})
f = open("C:/Users/Darek/.spyder-py3/sport/Sebastian Vettel.txt", "r")
content = f.read()
f.close()

newcontent = [content.replace(key, value) for key, value in d.items()]
print(newcontent)

#Zadanie 11
a = [1,2,12,4]
b = [2,4,2,8]

def scalar(first, second):
    if len(first) == len(second):
        s = 0
        for i in range(len(first)):
            s += first[i]*second[i]
        print(s)
    else:
        return "Vectors must have the same size"

scalar(a,b)

#Zadanie 12
def createMatrix(size):
    if size > 1:
        return [[random.randint(1,100) for x in range(size)] for y in range(size)]
    else:
        print("Error")

def sumOfMatrices(first, second):
    if len(first) == len(second):
        s = [[0 for x in range(len(first))] for y in range(len(first))]
        for i in range(len(first)):
            for j in range(len(first)):
                s[i][j] += first[i][j]+second[i][j]
        print(s)
    else:
        return "Matrices must have the same size"

a = createMatrix(128)
b = createMatrix(128)
sumOfMatrices(a,b)

#Zadanie 13
def createMatrix(size):
    if size > 1:
        return [[random.randint(1,100) for x in range(size)] for y in range(size)]
    else:
        print("Error")

def scalar(first, second):
    if len(first) == len(second):
        s = 0
        for i in range(len(first)):
            s += first[i]*second[i]
        return s
    else:
        return "Vectors must have the same size"

def productOfMatrices(first, second):
    if len(first) == len(second):
        s = [[0 for x in range(len(first))] for y in range(len(first))]
        for i in range(len(first)):
            for j in range(len(first)):
                s[i][j] = scalar(first[i], [row[j] for row in second])
        print(s)
    else:
        return "Matrices must have the same size"

a = createMatrix(8)
b = createMatrix(8)
print(a)
print(b)
productOfMatrices(a,b)
"""
#Zadanie 14
def createMatrix(size):
    if size > 1:
        return [[random.randint(1,100) for x in range(size)] for y in range(size)]
    else:
        print("Error")

def det(first, second):
    if len(first) == len(second):
        s = [[0 for x in range(len(first))] for y in range(len(first))]
        for i in range(len(first)):
            for j in range(len(first)):
                s[i][j] = scalar(first[i], [row[j] for row in second])
        print(s)
    else:
        return "Matrices must have the same size"

a = createMatrix(8)
b = createMatrix(8)
print(a)
print(b)
productOfMatrices(a,b)

"""
import numpy as np

a = np.zeros((2,2))
print(a)
"""






