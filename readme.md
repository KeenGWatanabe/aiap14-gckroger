Full Name: Goh Chee Keen Roger
email: mckeenweb@gmail.com
## Task 1 - Exploratory Data Analysis
## Summary of eda.ipynb
Accessing fishing.db file; 
Unfamiliar with SQL extraction, used SQLite DB Converter to .csv;
Check data types of fishing table; 
Evaluate Data Range with df.query; 
date call function of df;
created column 21;
Assigning groupings for easier plotting;
Test relation between humidity and rainfall;
Test relation between clouds and rainfall;
Create Boolean for 60%humdity and Highclouds and index them;
Create a pivot table from results;
Calculate Probability of attributes above 83.7% probability.

## Overview of Submitted folder
```
├── .github
├── src
│   └── (python files constituting the end-to-end ML pipeline in py.format)
├── README.md
└── eda.ipynb
├── requirements.txt
└── run.sh
```
## Task 2 - 
## Executing the pipeline
**Step 1) Data-preprocessing(eda_preprocessing.py)**
Imports the data from .db file, data is processed through the findings from EDA.ipnyb
Time constrain, unsuccessful query with SQLite, converted .db to .csv with SQlite converter and call with pd.csv

**Step 2) Data Preparation (data-prep.py)**
Numerical features will be pre-processed as required. The overall dataset untouched, just criteria specification like humid9am >= 60% call, and highclouds >= 7.

**Step 3) Look for Humidity60% and Clouds7**
The evaluation criteria for gridsearch are numerical and categorical.
 
**Step 4) Results**
Taking the best overall dataset previously found in step 3 and fed into the final model.

## Running of machine learning pipeline.
Machine learning model(probability formula) created with python 3 save as task2.py.





