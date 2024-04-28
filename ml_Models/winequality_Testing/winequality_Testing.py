import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import accuracy_score, classification_report

df= pd.read_csv('/content/winequality-red.csv')

df.shape

df.head()

#checking for missing value
df.isnull().sum()

#statistical values
df.describe()

#number of values for each quality
sns.catplot(x='quality', data=df, kind='count')

#volatile acidity vs quality
plot= plt.figure(figsize=(5,5))
sns.barplot(x='quality', y='volatile acidity', data=df)

#fixed acidity vs quality
plot= plt.figure(figsize=(5,5))
sns.barplot(x='quality', y='fixed acidity', data=df)

#citric acid vs quality
plot= plt.figure(figsize=(5,5))
sns.barplot(x='quality', y='citric acid', data=df)

cor= df.corr()

#heatmap
plt.figure(figsize=(10,10))
sns.heatmap(cor, cbar=True, square=True, fmt='.1f', annot=True, annot_kws={'size': 8}, cmap='Blues')

#seperate the data and label
columns_to_drop = ['quality', 'pH','chlorides', 'residual sugar']
#columns_to_drop = ['residual sugar','quality']
df1= df.drop(columns_to_drop, axis=1)
#df1= df.drop('quality', axis=1)

df1

df2= df['quality'].apply(lambda y_value: 1 if y_value>=7 else 0)

df2

x_train, x_test, y_train, y_test= train_test_split(df1, df2, test_size=0.2, random_state=3)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(x_train)
X_test = scaler.transform(x_test)

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Random Forest Classifier": RandomForestClassifier(n_estimators=100, random_state=185),
    "Support Vector Classifier": SVC(kernel='linear')
}

# Train and evaluate models
for name, model in models.items():
    print(f"Training {name}...")
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy of {name}: {accuracy}")
    print(classification_report(y_test, y_pred))
    print("="*50)

"""Random Forest Classifier"""

model= RandomForestClassifier(n_estimators=100, random_state=185)

model.fit(x_train, y_train)

x_test_pred= model.predict(x_test)
test_data_acc= accuracy_score(x_test_pred, y_test)

print(classification_report(y_test, x_test_pred))

print("Accuracy:", test_data_acc)

"""Prediction"""

input0=(7.9,0.6,0.06,15,59,0.9964,0.46,9.4)#quality value is 5
input1=(7.3,0.65,0,15,21,0.9946,0.47,10)#quality value is 7

input0_arr= np.array(input0)
input1_arr= np.array(input1)

inp0=input0_arr.reshape(1,-1)
inp1=input1_arr.reshape(1,-1)

def check_quality(arr):
  if model.predict(arr):
    print("Wine quality is Good")
  else:
    print("Wine quality is Bad")

check_quality(inp0)

check_quality(inp1)
