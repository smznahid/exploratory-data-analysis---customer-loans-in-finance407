import pandas as pd
import numpy as np
from scipy.stats import yeojohnson
from modules.get_information import DataFrameInfo


class DataTransform:

    '''
    class to transform data in a pandas DataFrame
    '''

    @staticmethod
    def convert_columns(df):
        '''
        a static method to convert different dtypes in my DataFrame.

        Args:
            df (pd.DataFrame): the DataFrame of which we want to convert the columns from
        Returns:
            None
        '''

        # grade, subgrade, home_ownership, loan_status, purpose, application_type, verification_status -> category
        df[['grade','sub_grade','home_ownership','loan_status','purpose','application_type','verification_status']] = df[['grade','sub_grade','home_ownership','loan_status','purpose','application_type','verification_status']].astype('category')
        # issue_date, earliest_credit_line, last_payment_date, next_payment_date, last_credit_pull_date -> datetime64[ns]
        datetime_list = ['issue_date', 'earliest_credit_line', 'last_payment_date', 'next_payment_date', 'last_credit_pull_date']
        for column in datetime_list:
            df[column] = pd.to_datetime(df[column], format='%b-%Y')
        
        # payment_plan -> bool
        df.payment_plan = df.payment_plan.astype('bool')
    

    @staticmethod
    def drop_columns(df: pd.DataFrame, columns: list):
       df.drop(columns=columns, inplace=True)
    
    @staticmethod
    def drop_null_rows_from_columns(df: pd.DataFrame, columns: list):
        df.dropna(subset=columns, inplace=True)

    @staticmethod
    def log_transform(df, column, y=0):
        transformation = df[column].map(lambda i: np.log(i+y) if i+y > 0 else 0)
        return transformation
    
    @staticmethod
    def boxcox_transform(df, column, lmbda=0):
        if lmbda != 0:
            transformation = df[column].map(lambda x: ((x**lmbda) - 1) / lmbda)
            return transformation
        else:
            transformation = df[column].map(lambda x: np.log(x) if x>0 else 0)
            return transformation
        
    
    @staticmethod
    def yeojohnson_transform(df, column):
        yeojohnson_transformation = df[column]
        yeojohnson_transformation = yeojohnson(yeojohnson_transformation)
        yeojohnson_transformation = yeojohnson(yeojohnson_transformation[:-1])
        yeojohnson_transformation = pd.Series(yeojohnson_transformation)
        return yeojohnson_transformation
    

    @staticmethod
    def remove_outliers(df, column):
        outliers = DataFrameInfo.find_outliers(df, column)
        df.drop(outliers.index.values, axis=0, inplace=True)
