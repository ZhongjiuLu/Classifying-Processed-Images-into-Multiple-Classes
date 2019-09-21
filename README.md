# Classifying Processed Images into Multiple Classes

Multi-label classification - Image Recognition 

## Introduction
We have processed images to represent as a vector of 300 attributes, The first 294 are decimal values in the range 0 to 1 inclusive. The next six are binary values describing whether the image had a beach, a sunset, plants, a field, mountains, and building respectively. A value of 1 describes that the scene was present and 0 means it was not. For example

\textbullet The vector <0.01,...,0,1,...,0.25,...,1,0,0,0,1,0> describes an image with a beach and mountains before processing
\textbullet The vector <0.01,...,0,1,...,0.25,...,0,1,1,0,0,1> describes an image with a sunset and buildings before processing
\textbullet The vector <0.01,...,0,1,...,0.25,...,0,0,0,1,0,0> describes an image with only a field before processing

## Note
The data provided is not based on the real images, so you should not try generating images from the dataset. You should build the training model using the given dataset only

## Task
You are given 1438 processed image data instances, the training dataset. You should build a model to predict how many scenes were present in 966 unseens processed image data instances in the testing dataset.

## Dataset
You are provided the training dataset in the file trian.csv. The file contains 1438 rows. Each row contains 300 comma-separated values. You are also provided the testing dataset in the file test.csv. The file contains 966 rows of 294 comma-separated values describing the attributes values.

## Submission Details
Write the code to build a model to predict how many types of scenes were present in the image before processing. The code must save the predictions to the file prediction.csv, which contains exactly 966 rows and each contains the six comma-separated binary values corresponding to the attribute values provided in the test.csv file

## Evaluation
The prediction accuracy of the model is calculated using accuracy score:
\textbullet Expected = ["0,0,0,0,1,1", "1,0,0,1,0,0"]
\textbullet Predicted = ["0,0,0,0,1,1", "1,0,1,0,0,1"]
\textbullet  Correct Prediction = ["Yes", "No"]

The correct number of predictions is 1, so the accuracy score is 1/2=0.5
