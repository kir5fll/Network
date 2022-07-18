import pandas as pd
from datetime import datetime

class DataPrepaire:
    df = None

    def __init__(self):
        """Constructor"""
        pass

    def open_file(self, _path_to_csv_file):
        self.df = pd.read_csv(_path_to_csv_file)

    def replace_string_value(self, _column_name):   #Замена строковых значений на числовое в соответствии
                                                    #с их индексом в словаре
        column_value = self.df[_column_name].value_counts()
        bd = dict(column_value)
        value_for_replace = 1
        for val in bd:
            self.df.loc[self.df[_column_name] == val, _column_name] = value_for_replace
            value_for_replace = value_for_replace+1

    def replace_nan_value(self, _column, _inserted_value):  #Замена пустых значений
        try:
            self.df[_column] = self.df[_column].fillna(_inserted_value)
        except Exception as e:
            print(e)

    def fill_empty_cell(self):  #Заменяем все пустые ячейки таблицы на числовое значение, которое
                                # #меньше на 1 минимального значения
        list_of_columns = self.df.columns.values #Определяем список колонок
        for val in list_of_columns:
            try:
                min_val_of_column = self.df[val].min()
                min_val_of_column = min_val_of_column - 1
                self.replace_nan_value(self, val, min_val_of_column)
            except Exception as e:
                print(e)

    def get_date_info(self, _column):   #Извлекается дополнительная информация
                                        # из даты - квартал и является ли эта дата выходным днём
        column_index = self.df.columns.get_loc(_column)
        list_of_weekend = []
        list_of_quarter = []

        progress_index = 0
        row_counter = 0
        border = 2000
        table_rows_count = self.df.shape[0]

        for index, row in self.df.iterrows():
            row_counter = row_counter + 1
            split_date_val = row[_column].split("/")  # mm.dd.yyyy
            d = datetime(int(split_date_val[2]), int(split_date_val[0]), int(split_date_val[1]))
            list_of_quarter.append(pd.Timestamp(row[_column]).quarter)

            is_this_weekend = 0
            if d.weekday() > 4:
                is_this_weekend = 1

            list_of_weekend.append(is_this_weekend)

            if row_counter == border:
                progress_index = progress_index + row_counter
                row_counter = 0
                print("Parse date. Progress " + str(progress_index) + " count of rows " + str(table_rows_count))

        progress_index = progress_index + row_counter
        print("Parse date. Progress " + str(progress_index) + " count of rows " + str(table_rows_count))

        self.df.insert(loc=column_index + 1, column=_column + "_weekend", value=list_of_weekend)
        self.df.insert(loc=column_index + 2, column=_column + "_quarter", value=list_of_quarter)

    def save_result(self, _path_to_file):
        self.df.to_csv(_path_to_file + ".prepaired", sep=',')