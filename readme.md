## Task 1 - Exploratory Data Analysis
df
## Overview of Submitted folder
```
├── .github
├── src
│   └── (python files constituting the end-to-end ML pipeline in py.fomrat)
├── README.md
└── eda.ipynb
├── requirements.txt
└── run.sh
```
## Executing the pipeline
**Step 1) Data-preprocessing(eda_preprocessing.py)**
Imports the data from .db file, data is processed through the findings from EDA.ipnyb

**Step 2) Data Preparation (data-prep.py)**
Data is prepared by one-hot encoding categorical features. Target encoding was done for ordinal features. Numerical features will be pre-processed as required. The overall dataset is also train-test split into 80/20 split.

**Step 3 & 4) Hyper Parameter tuning for Regression & Classification**
All hyper parameters are tuned through gridsearchCV through a predefined range^1^.
The evaluation criteria for regression and classification gridsearch are based on MAE of final test (numerical and categorical (1-10)).

 ^1^ In gridsearch CV the predefined hyperparameters has gone through multiple iterations previously to derive the optimal range. The grid can be expanded up to users discretion

**Step 4 & 5) Results**
Taking the best hyperparams previously found in step 3 and 4. the best parameters are fed into the final model and the results saved as a txt file
-> Since Classification is evaluated on an ordinal MAE, to calculate the true MAE, take ordinal MAE * 10.

## Running of machine learning pipeline.
Machine learning model created with python 3 and bash script.
### Installing dependencies
Paste the following command on your bash terminal to download dependencies
```sh
pip install -r requirements.txt
```
### Running the Machine Learning Pipeline
Past the followin command on your bash terminal to grant permission to execute the 'run.sh' file
```sh
chmod +x run.sh
```
Paste the following command on the bash terminal to run the machine learning programme
```sh
./run.sh
```




