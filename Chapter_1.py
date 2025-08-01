"""
  In this chapter we are see ...
  1. what is seabron ?
  2. why use seaborn and what is the different b/t matplotlib and Seaborn?
  3. how install seaborn.
"""



# what is seabron ?

'''
Seaborn is a library that uses Matplotlib underneath to plot graphs. 
It will be used to visualize random distributions.

'''

# why use seaborn and what is the different b/t matplotlib and Seaborn?
'''
Matplotlib: It is a Python library used for plotting graphs with the help of other libraries like Numpy and Pandas.
It is a powerful tool for visualizing data in Python.
It is used for creating statistical inferences and plotting 2D graphs of arrays.
It was first introduced by John D. Hunter in 2002. It
uses Pyplot to provide a MATLAB-like interface free and open-source. 
It is capable of dealing with various operating systems and their graphical backends.

Seaborn: It is also a Python library used for plotting graphs with the help of Matplotlib, Pandas, and Numpy.
It is built on the roof of Matplotlib and is considered as a superset of the Matplotlib library.
It helps in visualizing univariate and bivariate data. 
It uses beautiful themes for decorating Matplotlib graphics.
It acts as an important tool in picturing Linear Regression Models.
It serves in making graphs of statical Time-Series data. 
It eliminates the overlapping of graphs and also aids in their beautification.

'''
# how install seaborn.
'''
pip install seaborn
'''



# Small code for practice

import matplotlib.pyplot as plt
import pandas as pd

import seaborn as sns 


var_1=[1,2,3,4,5,6,7,8,9]
var_2=[4,5,6,1,2,3,7,8,9]

# we are not use  data direct so first that  data can conver into data frame

data_1=pd.DataFrame({"var_1":var_1,"var_2":var_2})


# we are create directly like sns.lineplot(x=var_1,y=var_2)

sns.lineplot(x="var_1",y="var_2",data=data_1)
plt.show()


