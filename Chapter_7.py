'''
In this chapter we create a  pairplot in seaborn.

def-->pairplot generates a grid of subplots. For each pair of numeric variables in the dataset,
it creates a scatter plot showing their bivariate distribution.

PairPlot --> sns.pairplit(dataset,vars=[particular set list ],hue="attribute name "
                          , palette="foe color", marker=["*","<"],
                          kind="which type of graph create",
                          hue_order=[],
                          x_vars=[],y_vars=[])
'''
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt 


var=pd.read_csv("D:\\Data Scientist\\Python\\Ad Python\\SeaBorn\\tips.csv").head(30)
# print(var)

# sns.pairplot(var,vars=["total_bill","tip"],hue="sex",hue_order=["Famale","Male"],palette="pink")
# plt.show()

'''
now we are see strip Plot in Seaborn.
def--> The seaborn.stripplot function creates a scatter plot where one of the variables is categorical and the 
other is continuous. It visualizes the distribution of individual data points along a single axis, often used
to complement other plots like box plots or violin plots to show the underlying distribution of observations.


Strip Plot --> sns.stripplot(x='",y="",data=dataset name,
                             hue= "attribute name",palette="Color name ",
                             linewidth=number ,edgecolor="color name",
                             jitter=number,size)
'''
m={"Male":"o","Famale":"<"}
sns.stripplot(x="day",y="total_bill",data=var,hue="sex",palette="Dark2",
              linewidth=1,edgecolor="y",size=10)
plt.show()