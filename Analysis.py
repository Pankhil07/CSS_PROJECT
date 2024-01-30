import numpy as np
import pandas as pd
from merge_stock_sentiment import merge_df
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import SGDClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import scale

keep_cols = ['score','Open','High','Low','Close','Adj Close','Volume','Label']
df = merge_df.copy()
df_1 = df[keep_cols]
X = df_1
X = X.drop(['Label'],axis=1)
X  = np.array(X)
y = np.array(df_1['Label'])
split = int(0.8 * len(df_1))
X_train = X[0:split]
y_train = y[0:split]

X_test = X[split:]
y_test = y[split:]

# print(X_train.shape)
# print(y_train.shape)
# print(X_test.shape)
# print(y_test.shape)
#model = LinearDiscriminantAnalysis().fit(X_train, y_train)
#model = KNeighborsClassifier(n_neighbors=10).fit(X_train,y_train)
#model = SGDClassifier(loss="hinge", penalty="l2", max_iter=100).fit(X_train,y_train)
model = RandomForestClassifier(n_estimators=100).fit(X_train,y_train)
#model = GaussianProcessClassifier().fit(X_train,y_train)
predictions = model.predict(X_test)
print(predictions)
print(y_test)

# Show model metrics
print(classification_report(y_test, predictions))