'''
In this chapter we are see how to create a barplot. barplot basecilly different two object or item.

sns.barplot(x="name",y="yname",data="dataframe name",hue ="fdata show two different option "
           , order = [we are set any print a graph], hue_order=[hue item order  ]
           , ci = that show error size, n_boot=that is -,
           orient="v"/"h",
           palette="that is use for color ".
           errcolor="y",errwidth=size,
           saturation =0.0 to 100,
           capsize=0.5)
           

'''


import pandas as pd 
import seaborn as sns 
from matplotlib import pyplot as plt

var=pd.read_csv("D:\Data Scientist\Python\Ad Python\SeaBorn\penguins.csv").head(9)
sns.barplot(x="bill_length_mm",y="bill_depth_mm",data=var,hue="sex")

plt.show()


###########################################################################################################

'''
Now next we are talk about the countplot .

seaborn.countplot() is a function within the Seaborn library in Python, used for visualizing the distribution
of categorical data. It displays the number of observations (counts) within each category of a given variable
using bars. Essentially, it functions as a histogram for categorical variables. 

countplot -> sns.countplot(x/y= "column name ",data=DATA_NAME ,hue="difference",saturation=0 to 1,palette="color")
'''
var1=pd.read_csv("D:\\Data Scientist\\Python\\Ad Python\\SeaBorn\\tips.csv")
sns.countplot(x="sex",data=var1,hue="smoker",saturation=0.5,palette="pink")
plt.show()