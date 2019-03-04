import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# reading and setting up the data and splitting into training and test sets
# for comments on this see the implementation of KNN
stock_DF = pd.read_csv("C:\\Users\\Tim\\Documents\\CrypTech\\" + "google.csv")
stock_DF = stock_DF.iloc[35:]

print("Data loaded")
df_feat = pd.DataFrame(stock_DF, columns=stock_DF.columns[1:-2])
X = df_feat
y = stock_DF['Winning']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

# training a single decision tree:
# TODO Visualize that tree
dtree = DecisionTreeClassifier()
dtree.fit(X_train, y_train)

predictions = dtree.predict(X_test)
print("Single Decision Tree:")
print(confusion_matrix(y_test, predictions))
print('\n')
print(classification_report(y_test, predictions))

# now training an actual random forest model
rfc = RandomForestClassifier(n_estimators=200)
rfc.fit(X_train, y_train)

rfc_pred = rfc.predict(X_test)
print("Random Forest:")
print(confusion_matrix(y_test, rfc_pred))
print('\n')
print(classification_report(y_test, rfc_pred))