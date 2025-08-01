'''
In this chapter we are see how to create a scatterplot graph .

A scatter graph, also known as a scatter plot or scatter diagram, is 
used to visualize the relationship betweentwo variables by plotting data
points on a two-dimensional plane.

Scatter graph -> sns.scatter(x="first var name ",
                            y="second var name ",
                            data=dataframe ,
                            marker=["o",'*'],
                            palette="color name ",
                            hue="that is show divide name ",
                            style="name attribute ",
                            size="size based on attribute",
                            sizes=(mannuailly),
                            alpha="visible range 0 to 1"
                            )
                            
'''

import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 

var =pd.read_csv("D:\Data Scientist\Python\Ad Python\SeaBorn\penguins.csv").head(20)
var = var.dropna()
# print(var.columns)
sns.scatterplot(x='bill_length_mm',y='bill_depth_mm',data=var,hue="sex",size="sex",
                sizes=(100,60),markers=["o","*"],palette="pink",
                alpha=0.5)
plt.show()