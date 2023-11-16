import pandas as pd


class DataFrameInfo:


    @staticmethod
    def datatypes(df):
        print(df.dtypes)

    @staticmethod
    def statistics(df):
        # return transposed .describe() as large number of columns.
        return df.describe().T
    
    @staticmethod
    def distinct_values(df):
        pass

    @staticmethod
    def df_shape(df):
        return df.shape()

    @staticmethod
    def percent_null(df):
        # TODO: percent_null
        pass