#imports
import numpy as np
from sklearn import svm
from sklearn.svm import SVR
import pandas as pd
from pandas import read_csv
import matplotlib.pyplot as plt
import random
from random import randrange
from csv import writer

#main code
df = read_csv("top_pandemics.csv")

y_initial = [] 
y_final = [] 
y = [] #y-coordinate

for pop in df["Global population lost"]:
    l = pop.split("[")
    y_initial.append(l[0])

for elements in y_initial:
    if "–" in elements:
        filter = elements.split("–")
        y_final.append(filter[1])
    else:
        y_final.append(elements) 

for elements in y_final:
    if elements != "":
        if "." not in elements:
            y.append(int(elements[:-1]))
        else:
            y.append(float(elements[:-1]))
    elif elements == "":
        y.append("Unknown")

print(y)

x_initial = []
x = []

for dates in df["Date"]:
    date = str(dates)
    d = date.split("–")
    x_initial.append(d[0])

for elements in x_initial:
    if "[" in elements:
        d = elements.split("[")
        x.append(d[0])
    else:
        x.append(elements)    

#print(x_initial)
print(x)

"""
x = []
for elements in df["Disease"]:
    x.append(elements)
        
plt.bar(x,y) 
plt.show() 
"""