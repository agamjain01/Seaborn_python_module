'''
 In this chapter we are are see the histogram in seaborn .
 
 Histograms are used to visualize the distribution of numerical data by grouping 
 it into bins and displaying the frequency of data points within each bin as a bar.
 
 Now how to create histogram -> displot("data name with attribute ",
                                        kde=true (kde means kranel density edge )
                                        bins=[number of range to cerate data ],
                                        log_scale=true ,
                                        rug=true (create bar scale  )
                                        color="color name "
                                        )
                            
'''

import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 


var =pd.read_csv("D:\Data Scientist\Python\Ad Python\SeaBorn\penguins.csv")
# print(var.columns)

sns.displot(var["flipper_length_mm"],bins=[170,180,190,200,220,230,240],kde=True,color="g",rug=True)

plt.show()