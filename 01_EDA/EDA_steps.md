**Steps of EDA**

Main steps involved while doing EDA are:

1. Loading Libraries
2. Setting interface i-e ignoring warnings, maximize views
3. Reading data
4. Data understanding i-e data type, columns,etc.
5. Checking null Data
6. Checking Outliers
7. 


---
___

Now dealing with the steps individually:
1. Setting the interface and smoothness of program

Ignoring warnings
```
        import warnings
        warning.filterwarning("ignore)
```
Maximum view settings
```
pd.set_option("display.max_rows",None)
pd.set_option("display.max_rows",None)
```
2. Reading the file

```
    pd.read_csv("path")
```
3. Data Understanding
```
df.head()
df.info()   # reveals the data type
df.describe()
df.columns
df.shape()  # shows rows vs columns
```
4. Checking the null values
```
df.isnull().sum()
df.isnull().sum()/len(df)   # calculating %
```