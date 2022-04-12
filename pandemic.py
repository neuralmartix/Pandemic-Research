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

df = read_csv('transmissibility.csv')

x = []
for elements in df["Year"]:
    x.append(elements)

y = []
for elements in df["Transmissibility"]:
    y.append(elements)

plt.plot(x,y)
plt.show()
