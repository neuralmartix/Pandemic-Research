import math
timerange = 100
pandemic_chance = 3.053

number_pandemics = 0
list_of_number_of_pandemics = []
years_masterlist = {}
years = []
starting_year = 2020
for i in range(1, 101):
  years_masterlist[2020+i] = 0
for i in range(10000): 
  starting_year=2020
  for i in range(100):
    starting_year+=1
    rn = random.randint(0,100)
    if(pandemic_chance>float(rn)):
      years.append(starting_year)
      number_pandemics+=1
  list_of_number_of_pandemics.append(number_pandemics)
  number_pandemics = 0
  for i in years:
   years_masterlist[i] += 1
  years = []
# print(list_of_number_of_pandemics)
# for i in range(1, 101):
#   print(2020+i)
#   print(years_masterlist[2020+i])
mean = 0
for i in list_of_number_of_pandemics:
  mean += i
print(mean/len(list_of_number_of_pandemics))
mean = 0
for i in range(1, 101):
  num = years_masterlist[2020+i]
  mean += num
print(mean/1000)
standard_deviation = 0
sum = 0
for i in range(1, 101):
  num = years_masterlist[2020+i]
  sum += (years_masterlist[2020+i]-mean/1000) * (years_masterlist[2020+i]-mean/1000)
sum = sum/1000
standard_deviation = math.sqrt(sum)
print(standard_deviation)
