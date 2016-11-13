import pandas as pd
import numpy as np

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif

data = pd.read_csv('df_all.csv')
data = data.fillna(value=0)
data = data.iloc[np.random.permutation(len(data))]
win_lose = data.reset_index(drop=True)['win/lose']

X = data.drop('win/lose', axis=1)[:]
y = data['win/lose'].values

X_new = SelectKBest(f_classif, k=50).fit_transform(X, y)

selected_features = pd.DataFrame(X_new)
selected_features = pd.concat([selected_features, win_lose], axis=1)

print selected_features

pd.DataFrame(selected_features).to_csv('selected_feature.csv')