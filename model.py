import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import joblib

data = pd.read_csv("data/iris.csv")
le = LabelEncoder()
print(le.fit(data['species']))
data['species'] = le.fit_transform(data['species'])
print(le.classes_) # ['Iris-setosa' 'Iris-versicolor' 'Iris-virginica']

X = data.drop(columns = ['species'])
y = data['species']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, y_train)

model_file = open("models/logistic_regression_model_iris_221122.pkl","wb")
joblib.dump(model, model_file)
model_file.close()