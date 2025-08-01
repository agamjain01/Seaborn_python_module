'''
In this chapter we are see how to create a Heatmap graph.

A heatmap in Seaborn is a graphical representation of data where individual values within a matrix are
displayed as colors. It is particularly useful for visualizing correlation matrices, showing patterns 
across two dimensions,or representing the magnitude of a phenomenon in a color-coded format.   


Heatmap -> sns.heatmap(dataset name , vmin=that range we started ,vmax=that range we end ,
                        cmap="that is use to color",annot=ture / false "that is visible that block number ",
                        annot_kws="that is change the size and color of the block",
                        linewidth=size "that is divide the block to the line ",
                        line_color="color name ',
                        cbar=ture/ false 
                        xticklabel=ture / false ,yticklabel=ture / false )
            data.set(xlabel="label name ",ylabel="label name ")
'''

import numpy as np
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 

var=np.linspace(1,10,10).reshape(2,5)

# sns.heatmap(var) # that is  craete a simple graph
# plt.show()


var_1=pd.read_csv("D:\\Data Scientist\\Python\\Ad Python\\SeaBorn\\anagrams.csv").head(10)

var_1=var_1.drop(["attnr"],axis=1)

v=sns.heatmap(var_1,vmin=0,vmax=12,cmap="pink",annot=True,annot_kws={"fontsize":10,"color":"r"},
            linewidths=10,linecolor="g",xticklabels=False,yticklabels=False,cbar=False)

v.set(xlabel="python",ylabel="Hello")
sns.set(font_scale=10)

plt.show()