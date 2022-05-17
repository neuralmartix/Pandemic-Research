import numpy as np
import pandas as pd
from sklearn import svm
from sklearn.svm import SVR
from pandas import read_csv
import matplotlib.pyplot as plt
import random
from random import randrange

years = 0
n_epochs = 100000
res1 = []
data1 = []
for i in range(n_epochs):
  year = 0
  #probs = float(randrange(325,496))/1000
  while True:
    rand = randrange(100000)
    if rand < (0.56*100000): 
      break
    else:
      years += 1
      year += 1

print(years/n_epochs)