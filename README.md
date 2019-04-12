# PUBG Finish Placement Prediction

## Project Charter

### Vision
Crack the winnning formula in PUBG and provide PUBG enthusiasts a platform to understand what it takes to win a game

### Mission
With over 50 million copies sold, PUBG is the fifth best selling game of all time, and has millions of active monthly players. With n number of different people playing with different strategies, it will be fun to know what helps you to win the game. What's the best strategy to win in PUBG? Should you sit in one spot and hide your way into victory, or do you need to be the top shot? Do you help/revive your teammates or let them die? The app will predict the finish placement based on the in-game statistics. Also the app will provide the user with the importance of features w.r.t final finish placement. PUBG enthusiasts can use the app to plan their game strategy and taste a tasty Chicken Dinner.

### Success Criteria

**Machine Learning Performance**: The model predicts the finish placement in PUBG based on the ingame stats. The finish placement is a continous varaible and hence cross-validation R-square of the prediction model will be a good measure of the model performance. Cross-validation R-square of anything above .70 is acceptable. Variable importance of the features and interpretability is an improtant performance metric as it helps the user to understand the features which maximizes their chance of winning.

**Business Outcome**: 
Number of app downloads is a good measure of pupularity and number of times the app is visited is a good measure of user enagement. User rating of the app is a good measure of app user satisfaction. A rating of 3.5 or above (on a scale of 5) would be acceptable.

## Planning

### Theme 

Create an app that suggests final finish placement for a given set of in-game charasteristics and enables desiging a better gaiming strategy   

### Epic

Prepare data, built model, design app and productionalize the app to predict finish placement in PUBG

##### Stories

 - **US0**: Find appropeiate PUBG dataset with relevant features
 - **US1**: Upload the dataset into a RDS
 - **US2**: Data preprocessing - cleaning missing, incoherent and incorrect data
 - **US3**: Exploratory Data Analysis - story generation and visualization
 - **US4**: Feature Engineering
 - **US5**: Prediction model selection and parameter tuning
 - **US6**: Model Evaluation
 - **US7**: Write unit tests to test each step of the model building process
 - **US8**: Create a front-end which accepts ingame statistics as user input and returns predictied finish placement 
 - **US9**: Create a script to feed user input to the model to get predictied finish placement
 - **US10**: Build a prediction pipeline in EC2 instance
 - **US11**: Create UAT cases to ensure the prediction pipeline does not break 
 - **US12**: Write script to log user input and error
 - **US13**: Deploy the app in production environment after UAT is passed
 
## Backlog
 - **Theme1.Epic1.US0** (2pts) - PLANNED: sprint 1
 - **Theme1.Epic1.US1** (1pt) - PLANNED: sprint 1
 - **Theme1.Epic1.US2** (2pt) - PLANNED: sprint 1
 - **Theme1.Epic1.US3** (4pt) - PLANNED: sprint 1
 - **Theme1.Epic1.US4** (4pt) - PLANNED: sprint 1
 - **Theme1.Epic1.US5** (4pt) - PLANNED: sprint 1
 - **Theme1.Epic1.US6** (4pt) - PLANNED: sprint 1
 - **Theme1.Epic1.US7** (2pt) - PLANNED: sprint 1
 - **Theme1.Epic1.US8** (4pt) - PLANNED: sprint 1
 - **Theme1.Epic1.US9** (2pt) - PLANNED: sprint 1
 - **Theme1.Epic1.US10** (2pt) - PLANNED: sprint 1
 - **Theme1.Epic1.US11** (2pt) - PLANNED: sprint 1
 - **Theme1.Epic1.US12** (1pt) - PLANNED: sprint 1
 - **Theme1.Epic1.US13** (2pt) - PLANNED: sprint 1
 
## Icebox
 
- Create a fancy front-end UI using D3
- Use spacial data to recommend the best places to land in a PUBG map

## Repo Structure

```├── README.md                         <- You are here
│
├── app
│   ├── static/                       <- CSS, JS files that remain static 
│   ├── templates/                    <- HTML (or other code) that is templated and changes based on a set of inputs
│   ├── models.py                     <- Creates the data model for the database connected to the Flask app 
│   ├── __init__.py                   <- Initializes the Flask app and database connection
│
├── config                            <- Directory for yaml configuration files for model training, scoring, etc
│   ├── logging/                      <- Configuration files for python loggers
│
├── data                              <- Folder that contains data used or generated. Only the external/ and sample/ subdirectories are tracked by git. 
│   ├── archive/                      <- Place to put archive data is no longer usabled. Not synced with git. 
│   ├── external/                     <- External data sources, will be synced with git
│   ├── sample/                       <- Sample data used for code development and testing, will be synced with git
│
├── docs                              <- A default Sphinx project; see sphinx-doc.org for details.
│
├── figures                           <- Generated graphics and figures to be used in reporting.
│
├── models                            <- Trained model objects (TMOs), model predictions, and/or model summaries
│   ├── archive                       <- No longer current models. This directory is included in the .gitignore and is not tracked by git
│
├── notebooks
│   ├── develop                       <- Current notebooks being used in development.
│   ├── deliver                       <- Notebooks shared with others. 
│   ├── archive                       <- Develop notebooks no longer being used.
│   ├── template.ipynb                <- Template notebook for analysis with useful imports and helper functions. 
│
├── src                               <- Source data for the project 
│   ├── archive/                      <- No longer current scripts.
│   ├── helpers/                      <- Helper scripts used in main src files 
│   ├── sql/                          <- SQL source code
│   ├── ingest_data.py                <- Script for ingesting data from different sources 
│   ├── generate_features.py          <- Script for cleaning and transforming data and generating features used for use in training and scoring.
│   ├── train_model.py                <- Script for training machine learning model(s)
│   ├── score_model.py                <- Script for scoring new predictions using a trained model.
│   ├── postprocess.py                <- Script for postprocessing predictions and model results
│   ├── evaluate_model.py             <- Script for evaluating model performance 
│
├── test                              <- Files necessary for running model tests (see documentation below) 

├── run.py                            <- Simplifies the execution of one or more of the src scripts 
├── app.py                            <- Flask wrapper for running the model 
├── config.py                         <- Configuration file for Flask app
├── requirements.txt                  <- Python package dependencies``` 
