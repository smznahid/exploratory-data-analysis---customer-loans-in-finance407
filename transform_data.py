import pandas as pd


class DataTransform:


    @staticmethod
    def convert_columns(df):
        # TODO: convert more columns, remove print statement.
        df.grade = df.grade.astype('category')
        print(df.dtypes)