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
from sklearn.linear_model import LinearRegression
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
    y_flights.append(math.log(int(sum)))

plt.scatter(x_flights, y_flights)
plt.show()

#second analysis of flights
df2 = read_csv("flights_2.csv")
x_fli = []
y_fli = []
for years in df2["Year"]:
    x_fli.append(years)
for elements in df2["Total"]:
    y_fli.append(math.log(elements))

plt.plot(x_fli,y_fli)
plt.show()
'''    
X = df2['Year'].to_numpy()[:-1].reshape(-1, 1)
y = df2["Total"].to_numpy()[:-1]
y = [float(i) for i in y]
'''