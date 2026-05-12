# bad_ml_model.py

# intentionally bad ML code for SonarQube testing

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# global variables (bad practice)
x = []
y = []

# duplicate code
def clean_data(df):
    df = df.dropna()
    df = df.drop_duplicates()
    return df

def clean_data_again(df):
    df = df.dropna()
    df = df.drop_duplicates()
    return df

# unnecessary nested loops
def useless_function():
    total = 0
    for i in range(100):
        for j in range(100):
            for k in range(100):
                total += i + j + k
    return total

# no exception handling
df = pd.read_csv("data.csv")

# random print debugging
print("starting model")
print("dataset shape:", df.shape)
print("dataset shape:", df.shape)

# magic numbers
df = df[df["age"] > 17]
df["salary"] = df["salary"] * 1.2345

# data leakage (bad ML practice)
X = df.drop("target", axis=1)
y = df["target"]

# train test split with no random state
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.5
)

# overfitting possibility
model = LinearRegression()

# training on all data accidentally
model.fit(X, y)

# unused variable
temp_variable = 12345

# hardcoded credentials (security issue)
password = "admin123"

# no evaluation metrics
predictions = model.predict(X_test)

# meaningless loop
for i in range(len(predictions)):
    print(predictions[i])

# inefficient dataframe iteration
for index, row in df.iterrows():
    print(row["age"])

# possible divide by zero
value = 10 / np.random.randint(0, 2)

# extremely long line (style issue)
print("this is a very very very very very very very very very very very very very very very very very very very very long line")

# dead code
if False:
    print("this will never run")

# duplicate condition
if len(df) > 0:
    print("data exists")
elif len(df) > 0:
    print("duplicate condition")

# no main function
print("finished")
