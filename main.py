import argparse
import sys
from dataprepaire import DataPrepaire
from networktrain import NetworkTrain
from work import Work
import joblib
import pandas as pd

programOptions = argparse.ArgumentParser(description="Program options")
programOptions.add_argument('--file_path', type=str, help="path to file")
programOptions.add_argument('--mode', type=str, help="work mode")

if __name__ == '__main__':
    args = programOptions.parse_args(sys.argv[1:])
    pathToFile = args.file_path
    workMode = args.mode

    if workMode == "data_prepaire": #file_path: train_dataset_train.csv
        print("Work mode is data_prepaire. File path: " + pathToFile)
        data_prepaire = DataPrepaire
        data_prepaire.open_file(data_prepaire, pathToFile)
        data_prepaire.replace_string_value(data_prepaire, 'ABC')
        data_prepaire.replace_string_value(data_prepaire, 'promo')
        data_prepaire.replace_string_value(data_prepaire, 'communication_type')
        data_prepaire.replace_string_value(data_prepaire, 'city')
        data_prepaire.replace_string_value(data_prepaire, 'country')
        data_prepaire.replace_string_value(data_prepaire, 'os')
        data_prepaire.replace_string_value(data_prepaire, 'browser')
        data_prepaire.replace_string_value(data_prepaire, 'platform')

        data_prepaire.get_date_info(data_prepaire, "month_id")
        data_prepaire.get_date_info(data_prepaire, "carts_created_at")

        data_prepaire.fill_empty_cell(data_prepaire)

        data_prepaire.save_result(data_prepaire, pathToFile)
    elif workMode == "train": #file_path: train_dataset_train.csv.prepaired
        print("Work mode is train. File path: " + pathToFile)
        network_train = NetworkTrain
        network_train.open_file(network_train, pathToFile)
        network_train.prapair_data(network_train)
        network_train.train_network(network_train)
        network_train.save_model(network_train, 'model.pkl')
    elif workMode == "work": #file_path: test_dataset_test.csv
        print("Work mode is work. File path: " + pathToFile)
        work_model = Work
        #work_model.model_work(work_model, pathToFile)

        work_model.open_file(work_model, pathToFile)
        work_model.prepair_data(work_model)
        work_model.load_model(work_model, "model.pkl")
        work_model.work(work_model)
        work_model.save_work_result(work_model, pathToFile + ".result")