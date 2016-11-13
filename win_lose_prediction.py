import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.cross_validation import StratifiedKFold
from sklearn.feature_selection import RFECV
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif


data = pd.read_csv('df_all.csv')
data = data.fillna(value=0)
data = data.iloc[np.random.permutation(len(data))]
data_train = data[0:250]
data_test = data[250::]

classifier = RandomForestClassifier(n_estimators=100)

X = data_train.drop('win/lose', axis=1)[:]
y = data_train['win/lose'].values
X_test = data_test.drop('win/lose', axis=1)[:]
y_test = data_test['win/lose'].values

classifier.fit(X, y)
predict = classifier.predict(X_test)

count = 0
for i in xrange(len(y_test)):
    if y_test[i] == predict[i]:
        count += 1
print 'accuracy using all features ', 1.0*count/len(y_test)

selected_feature = pd.read_csv('selected_feature.csv')
X = selected_feature[0:150].drop('win/lose', axis=1)
y = selected_feature[0:150]['win/lose'].values
X_test = selected_feature[150::].drop('win/lose', axis=1)
y_test = selected_feature[150::]['win/lose'].values
classifier.fit(X, y)
predict = classifier.predict(X_test)

count = 0
for i in xrange(len(y_test)):
    if y_test[i] == predict[i]:
        count += 1
print 'accuracy using selected features: ', 1.0*count/len(y_test)


# print X.shape
# X_new = SelectKBest(f_classif, k=50).fit_transform(X, y)
# print X_new.shape
#
# svc = SVC(kernel="linear")
# rfecv = RFECV(estimator=svc, step=1, cv=StratifiedKFold(y, 2),
#               scoring='accuracy')
# rfecv.fit(X, y)
# print("Optimal number of features : %d" % rfecv.n_features_)
# # Plot number of features VS. cross-validation scores
# plt.figure()
# plt.xlabel("Number of features selected")
# plt.ylabel("Cross validation score (nb of correct classifications)")
# plt.plot(range(1, len(rfecv.grid_scores_) + 1), rfecv.grid_scores_)
# plt.show()