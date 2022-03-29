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
y_final = [] #y-coordinate

for deaths in df["Death"]:
    l = deaths.split(" ")
    y_initial.append(l[0])

for elements in y_initial:
    if "–" in elements:
        filter = elements.split("–")
        if "." in filter[1]:
            y_final.append(float(filter[1]))
        else:
            y_final.append(int(filter[1]))    
    else:
        if "." in elements:
            y_final.append(float(elements))
        else:
            y_final.append(int(elements))  

print(y_final)            

        