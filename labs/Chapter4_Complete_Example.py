# Chapter 4: Complete Example - Train and Test an AI Intrusion Detector
# Course 314341, Ajloun National University. Data: Train_data.csv (Kaggle sampadab17/network-intrusion-detection)

# 1  Load the data
import pandas as pd
data = pd.read_csv("Train_data.csv")
print(data.shape)
print(data.head())

# 2  Features (X) and label (y)
X = data.drop(columns=["class"])
y = data["class"]
print(y.value_counts())

# 3  Text columns -> numbers (one-hot)
X = pd.get_dummies(X,
      columns=["protocol_type", "service", "flag"])
print(X.shape)

# 4  Split: 70% training, 30% test
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, stratify=y, random_state=42)

# 5  Train a decision tree
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(max_depth=5,
                               random_state=42)
model.fit(X_train, y_train)

# 6  Test on unseen data
y_pred = model.predict(X_test)

# 7  Measure the detector
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
print(confusion_matrix(y_test, y_pred,
                       labels=["anomaly", "normal"]))
print(classification_report(y_test, y_pred))

# Extra 1  Try trees of different depths (overfitting)
for depth in [1, 5, None]:
    m = DecisionTreeClassifier(max_depth=depth,
                               random_state=42)
    m.fit(X_train, y_train)
    print(depth, round(m.score(X_train, y_train), 2),
                 round(m.score(X_test, y_test), 2))

# Extra 2  Print the rules the tree learned
from sklearn.tree import export_text
print(export_text(model, feature_names=list(X.columns),
                  max_depth=2))

# Extra 3  Change the alarm limit
scores = model.predict_proba(X_test)[:, 0]  # chance of anomaly
for limit in [0.3, 0.5, 0.8]:
    alarm = scores >= limit
    caught = (alarm & (y_test == "anomaly")).sum()
    false_alarms = (alarm & (y_test == "normal")).sum()
    print(limit, caught, false_alarms)

# Extra 4  Compare with k-nearest neighbours
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler().fit(X_train)  # training only!
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(scaler.transform(X_train), y_train)
y_knn = knn.predict(scaler.transform(X_test))
print(classification_report(y_test, y_knn))
