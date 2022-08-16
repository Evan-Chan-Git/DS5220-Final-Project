import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv('https://raw.githubusercontent.com/Evan-Chan-NEU/DS5220-Final-Project/main/Project%20Dataset/Stores.csv')

corr=df.corr()
sns.heatmap(corr,linewidths=1,linecolor='white',annot=True)
