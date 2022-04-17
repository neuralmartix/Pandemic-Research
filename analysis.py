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

#transmissibility
df = read_csv("transmissibility.csv")
x = []
for years in df["Year"]:
    x.append(years)
y = []
for index in df["Transmissibility"]:
    y.append(index)

plt.scatter(x,y)
plt.show() 

#communications internationally
df2 = read_csv("flights.csv")
x_flights = []
for years in range(2006,2020):
    sum = 0
    for elements in df2["{}".format(years)]:
        if elements == "":
            sum = sum + 0
        elif elements != "":
            try:
                elements  = float(elements)
        sum = sum + elements
            except KeyError:
                sum = sum + 0
        x_flights.append(sum)

print(x_flights)

