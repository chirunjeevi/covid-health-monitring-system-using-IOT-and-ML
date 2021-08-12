import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

temperature_sample=input("enter Temperature value:")
oxidation_sample = input("Enter oxidation value:")

data = pd.read_csv('dataset.csv')
x = data[['temperature','oxidiation']].values
y = data['status'].values
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
regressor = RandomForestClassifier(n_estimators=200)
regressor.fit(x_train,y_train)

new_input= [[temperature_sample,oxidation_sample]]
predicted_output = regressor.predict(new_input)
print(predicted_output)
if(predicted_output == 0):
    print("Healthy person")
else:
    print("Covid patient")
    







