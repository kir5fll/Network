import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import recall_score, precision_score
class Work:
    df = None
    X = None
    model = None
    pred = None

    def __init__(self):
        """Constructor"""
        pass

    def open_file(self, _path_to_csv_file):
        self.df = pd.read_csv(_path_to_csv_file)

    def prepair_data(self):
        self.df.dtypes[self.df.dtypes == "object"].values
        mass_object = self.df.dtypes[self.df.dtypes == "object"].index.values
        self.X = self.df.drop(mass_object, axis=1)

    def load_model(self, _model_path):
        self.model = joblib.load(_model_path)

    def work(self):
        self.pred = self.model.predict(self.X)

    def save_work_result(self, _result_path):
        self.df.insert(loc=len(self.df.columns), column="network_result", value=self.pred)
        self.df.to_csv(_result_path, sep=',')
        print(self.pred)

    def model_work(self, _path_to_csv_file):
        df = pd.read_csv(_path_to_csv_file)

        df.dtypes[df.dtypes == "object"].values
        mass_object = df.dtypes[df.dtypes == "object"].index.values
        X = df.drop(mass_object, axis=1)

        fittedModel = joblib.load("model.pkl")
        pred = fittedModel.predict(X)
        df.insert(loc=len(df.columns), column="network_result", value=pred)
        df.to_csv(_path_to_csv_file + ".result", sep=',')
        print(pred)