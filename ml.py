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

df2 = read_csv("new_file.csv")
res = df2.sort_values('Outbreak')

x = []
for dates in res['Outbreak']:
    x.append(dates)

y = []
for percentages in res["Percentage of Global Population Lost"]:
    y.append(percentages)

plt.plot(x, y)
plt.show()

print(res["Outbreak"])
'''
res = res.groupby(by=["Outbreak"]).sum()
X = res.index.to_numpy().reshape(-1, 1)
y = res.to_numpy()
clf = svm.SVC()
clf.fit(X, y)
years_want_to_predict = np.array(range(2020,2200)).reshape(-1, 1)
results = clf.predict(years_want_to_predict)

print(results)
'''