import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import recall_score, precision_score
import joblib

class NetworkTrain:

    df = None
    X = None
    y = None
    clf = None

    def __init__(self):
        """Constructor"""
        pass

    def open_file(self, _path_to_csv_file):
        self.df = pd.read_csv(_path_to_csv_file)

    def prapair_data(self):
        mass_object = self.df.dtypes[self.df.dtypes == "object"].index.values
        mass_object = np.append(mass_object, "target")
        self.X = self.df.drop(mass_object, axis=1)
        self.y = self.df[["target"]]

    def train_network(self):
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.1, random_state=42)
        self.clf = RandomForestClassifier(random_state=0)
        self.clf.fit(X_train, y_train.values.ravel())
        pred = self.clf.predict(X_test)
        print(y_test)
        print(0.2 * recall_score(y_test, pred, average='macro') + 0.8 * precision_score(y_test, pred, average='macro'))

    def save_model(self, _path):
        joblib.dump(self.clf, _path)
