'''
In this chapter we are see load the data set form online and internal data.
so we are use seaborn.load_dataset(that is use for online data set)

sns.lineplot(x="data name ",y="second data set",data="load data set name",hue="data show different dataset name "
                style="show data name",palette="color",marker=["o","^"],dashes=False / ture,legend=ture / false)
                
'''

import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd

x_1=pd.read_csv("D:\Data Scientist\Python\Ad Python\SeaBorn\zomato.csv").head(10)
# 'rate', 'votes'


sns.lineplot(x="rate",y="votes",data=x_1,hue="location",size=50,style="location",markers=["o","^"],palette="pink",
             dashes=False,legend=True)

plt.grid()
plt.title("Zomato data ")

plt.show()