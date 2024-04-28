**Steps of EDA**

Main steps involved while doing EDA are:

Steps of EDA 
1. Define the objective: 

   - Clearly articulate the research question or problem you want to address through EDA. 

   - Identify the specific aspects of the dataset you need to investigate to answer your question. 

2. Gather the data: 

   - Identify relevant data sources such as databases, files, APIs, or web scraping. 

   - Access and retrieve the data from the identified sources. 

   - Ensure data integrity by verifying its accuracy, completeness, and consistency. 

3. Load the data: 

   - Import the dataset into your preferred data analysis environment using appropriate libraries or tools. 

   - Choose the appropriate data structure (e.g., data frame, array) to hold the data in memory. 

4. Explore the structure of the dataset: 

   - Use functions or methods to examine the dimensions of the dataset (number of rows and columns). 

   - Investigate the data types of each column (numeric, categorical, datetime, etc.). 

   - Check for missing values in the dataset and determine their distribution. 

5. Handle missing data: 

   - Identify the nature and patterns of missing data (random, systematic, or missing completely at random). 

   - Decide on the appropriate strategy for handling missing data, such as imputation, deletion, or modeling. 

   - Apply the chosen strategy to deal with missing values and update the dataset accordingly. 

6. Clean the data: 

   - Identify and handle outliers, inconsistencies, or errors in the dataset. 

   - Correct any obvious mistakes or discrepancies in the data. 

   - Standardize or normalize data formats, units, or scales for consistency. 

7. Summarize the data: 

   - Calculate basic summary statistics, such as mean, median, mode, standard deviation, minimum, maximum, etc., for numerical variables. 

   - Determine the distribution of variables through measures like skewness and kurtosis. 

   - Summarize categorical variables using frequency counts or proportions. 

8. Visualize the data: 

   - Create various plots and charts, such as histograms, scatter plots, bar charts, box plots, and heatmaps, to depict the data visually. 

   - Customize visualizations to highlight patterns, relationships, or distributions of interest. 

   - Label axes, add legends, and provide appropriate titles for better interpretability. 

9. Identify outliers: 

   - Use statistical methods (e.g., z-scores, interquartile range) or domain knowledge to detect potential outliers. 

   - Visualize outliers using box plots, scatter plots, or other relevant plots. 

   - Investigate the reasons behind outliers and determine whether they are genuine anomalies or errors. 

10. Analyze relationships: 

    - Calculate correlation coefficients (e.g., Pearson, Spearman) to measure the strength and direction of relationships between variables. 

    - Perform cross-tabulations or contingency tables to explore associations between categorical variables. 

    - Conduct regression analysis to assess the linear relationship between variables. 

11. Perform feature engineering: 

    - Create new features by transforming existing variables (e.g., logarithmic transformations, polynomial features). 

    - Aggregate or group variables to create meaningful higher-level features. 

    - Explore interactions between variables by multiplying or combining them. 

12. Conduct hypothesis testing: 

    - Formulate null and alternative hypotheses based on the research question. 

    - Choose appropriate statistical tests (e.g., t-tests, chi-square tests, ANOVA) based on the data and hypothesis. 

    - Calculate test statistics, p-values, and confidence intervals to evaluate the significance of results. 

13. Document findings: 

    - Summarize key insights, patterns, and relationships discovered during the EDA process. 

    - Create clear and concise visualizations, tables, or charts to communicate the findings effectively. 

    - Provide interpretations and recommendations based on the results, considering the original research question. 

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

