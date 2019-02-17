#  Online-Bidding-Human-or-Robot
_____
![Bot Pic](https://storage.googleapis.com/kaggle-competitions/kaggle/4294/media/robot_banner@.png)

# Table of contents
1. [Introduction](#Introduction)
2. [Goal](#Goal)
3. [Dataset](#Dataset)
4. [Data Exploration](#Data&#32;Exploration)
4. [Feature Extraction](#Feature&#32;Extraction)
5. [Models](#Models)
6. [Best Model](#Best&#32;Model)
7. [File Structure](#File&#32;Structure)

## Introduction
This project is about classifying bidder as human or bot in an online auction. Where human are becoming increasingly frustrated with their inability to win auctions vs. Bots. As a result, usage from the site's core customer base is decreasing.

## Goal
The goal of this project is to identify online auction bids that are placed by "robots", helping the site owners easily flag these users for removal from their site to prevent unfair auction activity. 

## Dataset
[Kaggle:facebook-recruiting-iv-human-or-bot/data](https://www.kaggle.com/c/facebook-recruiting-iv-human-or-bot/data)
Bidder information, which is basically the IDs and labels (robot or human) of bidders (labels of test bidders are not given). Although some information about payment account and address is also provided, the obfuscation for
privacy makes them useless.

## Data&#32;Exploration
By basic statistics, I find some distinguish patterns between humans and robots: (1) Bots have more bids in auctions, and can be more active, e.g., robots bid more quickly.
(2) Bots win more auctions, which is not surprising because they are designed to win auctions. 

## Feature&#32;Extraction 
I extracted a list of features with the help of bids and train datasets.

## Models
1. Logistic Regresstion
2. KNN Model
3. Decision Tree Model
4. Random Forest Model
5. Naive Bayes Model
6. SVM (Linear)

## Best&#32;Model 
Decision KNN Model 

## Score&#32;Table
| Model       | F1 Score         | 
| ------------- |:-------------:|
|Logistic Regression| 0.788 | 
| **KNN**     | **0.916**   |  
| Decision Tree | 0.914    |    |
| Random Forest | 0.975     |    |
| SVM | 0.794|    |
| Naive Bayes|0.568  |    |


## File&#32;Structure
```
Project
│   README.md
└───  DataSet
   │   bids.csv
   │   train.csv
   |   test.csv
└───  Jupyter  Notebooks
   │   DataExploration.ipynb
   │   FeatureExtraction.ipynb
   │   DataBalancing.ipynb
   │   ModelFitting.ipynb
   │   FeatureExtraction.ipynb
└───  DumanVSBot App
   │   Data
       │   bids.csv
       | knn_model_iris.pkl
   │   Static
       │   train.csv
   │   templates
       │   index.html
└───  Presentation
   │   OnlineBidding_HumanVSBot.pptx
```