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
        return df.nunique()

    @staticmethod
    def df_shape(df):
        return df.shape()

    @staticmethod
    def percent_null(df):
        null_values = df.isnull().sum() # sum of null values
        total_values = len(df)
        percentage_null = null_values / total_values * 100
        return percentage_null
    
    @staticmethod
    def count_values(df, column):
        return df[column].value_counts()
    
    @staticmethod
    def get_null_greater_than_zero(df):
        null_values = DataFrameInfo.percent_null(df)
        return null_values[null_values > 0]
    
    @staticmethod
    def find_outliers(df, column):
        Q1 = df[column].quantile(0.25) # first quartile
        Q3 = df[column].quantile(0.75) # third quartile

        IQR = Q3 - Q1 # inter-quartile range.

        outliers = df[((df[column] < (Q1 - 1.5 * IQR)) | (df[column] > (Q3 + 1.5 * IQR)))][column]
        return outliers
    