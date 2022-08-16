# DS5220-Final-Project

# Intro
The purpose of this repository is to contain the results of my DS5220 final project.  The instructions for this project can be found in the Project Guidlines folder.  The publicily available dataset used in this exploratory data analysis, [Supermarket store branches sales analysis](https://www.kaggle.com/datasets/surajjha101/stores-area-and-sales-data), can be found on [kaggle](https://www.kaggle.com/).

# Exploring the Data

First we visualize the first five rows of the data to understand the features.
```
	Store ID	Store_Area	Items_Available	Daily_Customer_Count	Store_Sales
0	       1	      1659	           1961	                 530	      66490
1	       2	      1461	           1752	                 210	      39820
2	       3	      1340	           1609	                 720	      54010
3	       4	      1451	           1748	                 620	      53730
4	       5	      1770	           2111	                 450	      46620
```

Next we find out if there are any empty cells in the dataset.

```
Store ID                0
Store_Area              0
Items_Available         0
Daily_Customer_Count    0
Store_Sales             0
dtype: int64
```

Next we create a pairs plot (below) to understand the data struture.  The diagonal plots show us that the variables are normally distibuted and centrally concentrated. There is also a visible linear relationship between Store Area and Items available.

<img src="figs/fig1.png" width="500">

```
python src/src1.py
```

Next we create a heatmap (below) to further visualize the correlation of various features.

<img src="figs/fig2.png" width="500">

```
python src/src2.py
```
