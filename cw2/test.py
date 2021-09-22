import pandas as pd

names = ['sepalLength', 'sepalWidth', 'petalLength', 'petalWidth', 'class']
iris = pd.read_csv('iris.data', sep=',', names=names)
'''
#1
iris.min()
iris.max()
for item in names:
    print(item +"[" + str(iris[item].min()) + "," + str(iris[item].max()) + "]")
iris.mean()
iris.std()
iris.var()
iris.count()
iris.quantile(q=0.25)
iris.quantile(q=0.5)
iris.quantile(q=0.75)
'''
import matplotlib.pyplot as plt
features=iris[['sepalLength', 'sepalWidth', 'petalLength', 'petalWidth']]
labels='sepalLength', 'sepalWidth', 'petalLength', 'petalWidth'
#2

plt.figure()
4
plt.hist(iris['sepalLength'])
plt.xlabel("sepalLength")
plt.subplot(222)
plt.hist(iris['sepalWidth'])
plt.xlabel("sepalWidth")
plt.subplot(223)
plt.hist(iris['petalLength'])
plt.xlabel("petalLength")
plt.subplot(224)
plt.hist(iris['petalWidth'])
plt.xlabel("petalWidth")
plt.show()

#2.2
plt.figure()
plt.boxplot([iris['sepalLength'], iris['sepalWidth'], iris['petalLength'], iris['petalWidth']], labels=labels)
plt.show()

#2.3
plt.figure()
i=1
for item1 in features:
    for item2 in features:
        plt.subplot(4,4,i)
        i+=1
        plt.scatter(iris[item1], iris[item2])
        plt.xlabel(item1)
        plt.ylabel(item2)
plt.show()

#2.4
plt.figure()
i=1
for item in features:
    plt.subplot(3,4,i)
    plt.hist(iris[iris['class'] == "Iris-setosa"][item])
    plt.ylabel("Iris-setosa")
    plt.xlabel(item)
    plt.subplot(3,4,i+4)
    plt.hist(iris[iris['class'] == "Iris-versicolor"][item])
    plt.ylabel("Iris-versicolor")
    plt.xlabel(item)
    plt.subplot(3,4,i+8)
    plt.hist(iris[iris['class'] == "Iris-virginica"][item])
    plt.ylabel("Iris-virginica")
    plt.xlabel(item)
    i+=1
plt.show()

'''
import numpy as np
air = pd.read_excel('AirQualityUCI.xlsx')

for item in air.columns[2:]:
    a = air[item].quantile(0.75)
    b = air[item].quantile(0.25)
air[(air[item]>=(a-b)*1.5+a)|(air[item]<=b-(a-b)*1.5)]=np.nan
air.fillna(air.median(),inplace=True)
'''
'''
print(air.head())
print(air.min())
print(air.max())
#for item in air.columns:
#    print(item +"[" + str(air[item].min()) + "," + str(air[item].max()) + "]")
print(air[air.columns[1:]].mean())
print(air.std())
print(air.var())
print(air.count())
print(air.quantile(q=0.25))
print(air.quantile(q=0.5))
print(air.quantile(q=0.75))

import matplotlib.pyplot as plt
plt.figure()
i=1
for item in air.columns[2:]:
    plt.subplot(3,5,i)
    plt.hist(air[item])
    i+=1
plt.show()

features=air.columns[2:]
plt.figure()
plt.boxplot([air[features[0]],air[features[1]],air[features[2]],air[features[3]],air[features[4]],air[features[5]],air[features[6]],air[features[7]],air[features[8]],air[features[9]],air[features[10]],air[features[11]],air[features[12]]])
plt.show()

plt.figure()
plt.boxplot([air[features[0]],air[features[1]],air[features[2]],air[features[3]],air[features[4]],air[features[5]],air[features[6]],air[features[7]],air[features[8]],air[features[9]],air[features[10]],air[features[11]],air[features[12]]],showfliers=False)
plt.show()
'''