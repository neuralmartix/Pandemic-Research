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
import math
from scipy.optimize import curve_fit
'''
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
'''
#communications internationally
df2 = read_csv("flights.csv")
y_flights = []
x_flights = []
for years in range(1970,2021):
    x_flights.append(years)
    sum = 0
    for elements in df2["{}".format(years)]:
        if math.isnan(elements) == False:
            sum = sum + elements
    y_flights.append(int(sum))

print(len(y_flights))
print(len(x_flights))    
plt.scatter(x_flights, y_flights)
#plt.plot(x_flights, y_fit, color='r')
plt.show()

