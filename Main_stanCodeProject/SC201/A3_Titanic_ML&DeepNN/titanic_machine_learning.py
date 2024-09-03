"""
File: titanic_machine_learning.py
Name: Blair
----------------------------------
This file builds a machine learning algorithm by pandas and sklearn libraries.
We'll be using pandas to read in dataset, store data into a DataFrame,
standardize the data by sklearn, and finally train the model and
test it on kaggle website. Hyper-parameters tuning are not required due to its
high level of abstraction, which makes it easier to use but less flexible.
You should find a good model that surpasses 77% test accuracy on kaggle.
"""

import math
import pandas as pd
from sklearn import preprocessing, linear_model

TRAIN_FILE = 'titanic_data/train.csv'
TEST_FILE = 'titanic_data/test.csv'


def data_preprocess(filename, mode='Train', training_data=None):
    """
    :param filename: str, the filename to be read into pandas
    :param mode: str, indicating the mode we are using (either Train or Test)
    :param training_data: DataFrame, a 2D data structure that looks like an excel worksheet
                          (You will only use this when mode == 'Test')
    :return: Tuple(data, labels), if the mode is 'Train'; or return data, if the mode is 'Test'
    """
    data = pd.read_csv(filename)
    labels = None
    if mode == 'Train':
        features = ['Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
    elif mode == 'Test':
        features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
    data = data[features]
    if mode == 'Train':
        data = data.dropna()
        labels = data.pop('Survived')
    elif mode == 'Test':
        age_avg = round(training_data.Age.mean(), 3)
        data.Age.fillna(age_avg, inplace=True)
        fare_avg = round(training_data.Fare.mean(), 3)
        data.Fare.fillna(fare_avg, inplace=True)
    data.Sex.replace(['male', 'female'], [1, 0], inplace=True)
    data.Embarked.replace(['S', 'C', 'Q'], [0, 1, 2], inplace=True)

    if mode == 'Train':
        return data, labels
    elif mode == 'Test':
        return data


def one_hot_encoding(data, feature):
    """
    :param data: DataFrame, key is the column name, value is its data
    :param feature: str, the column name of interest
    :return data: DataFrame, remove the feature column and add its one-hot encoding features
    """

    data = pd.get_dummies(data, columns=[feature])

    return data


def standardization(data, mode='Train'):
    """
    :param data: DataFrame, key is the column name, value is its data
    :param mode: str, indicating the mode we are using (either Train or Test)
    :return data: DataFrame, standardized features
    """
    standard = preprocessing.StandardScaler()
    if mode == 'Train':
        data = standard.fit_transform(data)
    else:
        data = standard.transform(data)
    return data


def main():
    """
    You should call data_preprocess(), one_hot_encoding(), and
     on your training data. You should see ~80% accuracy on degree1;
    ~83% on degree2; ~87% on degree3.
    Please write down the accuracy for degree1, 2, and 3 respectively below
    (rounding accuracies to 8 decimal places)
    TODO: real accuracy on degree1 -> 0.80196629
    TODO: real accuracy on degree2 -> 0.83707865
    TODO: real accuracy on degree3 -> 0.87640449
    """

    # Data cleaning
    data_train, labels = data_preprocess(TRAIN_FILE, mode='Train', training_data=None)
    data_train = one_hot_encoding(data_train, 'Sex')
    data_train = one_hot_encoding(data_train, 'Pclass')
    data_train = one_hot_encoding(data_train, 'Embarked')

    # Normalization / Standardization
    standardizer = preprocessing.StandardScaler()
    data_train = standardizer.fit_transform(data_train)

    # Degree 1 Polynomial Model #
    h1 = linear_model.LogisticRegression(max_iter=10000)
    classifier_h1 = h1.fit(data_train, labels)
    print('Degree 1 Training Acc:', round(classifier_h1.score(data_train, labels), 8))

    # Degree 2 Polynomial Model #
    h2 = linear_model.LogisticRegression(max_iter=10000)
    poly_phi_extractor_2 = preprocessing.PolynomialFeatures(degree=2)
    train_data_poly_2 = poly_phi_extractor_2.fit_transform(data_train)
    classifier_h2 = h2.fit(train_data_poly_2, labels)
    print('Degree 2 Training Acc:', round(classifier_h2.score(train_data_poly_2, labels), 8))

    # Degree 3 Polynomial Model #
    h3 = linear_model.LogisticRegression(max_iter=10000)
    poly_phi_extractor_3 = preprocessing.PolynomialFeatures(degree=3)
    train_data_poly_3 = poly_phi_extractor_3.fit_transform(data_train)
    classifier_h3 = h3.fit(train_data_poly_3, labels)
    print('Degree 3 Training Acc:', round(classifier_h3.score(train_data_poly_3, labels), 8))


if __name__ == '__main__':
    main()
