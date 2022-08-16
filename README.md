# DS5220-Final-Project

# Intro
The purpose of this repository is to contain the results of my DS5220 final project.  The instructions for this project can be found in the Project Guidlines folder.  The publicily available dataset used in this exploratory data analysis, [Supermarket store branches sales analysis](https://www.kaggle.com/datasets/surajjha101/stores-area-and-sales-data), can be found on [kaggle](https://www.kaggle.com/).

# Exploring the Data

First we find out  if there are any empty cells in the dataset.

```
Store ID                0
Store_Area              0
Items_Available         0
Daily_Customer_Count    0
Store_Sales             0
dtype: int64
```

```
python src/src1.py
```



<img src="figs/fig1.png" width="500">

Recreate this figure (above) using 

```
python src/src2.py
```

Next we create a heatmap (below) to visualize the correlation of various features.

<img src="figs/fig2.png" width="500">

Recreate this figure (above) using 

```
python src/src3.py
```
