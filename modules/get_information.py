import pandas as pd


class DataFrameInfo:


    '''
    A Class used to extract information from a dataframe.
    '''

    @staticmethod
    def datatypes(df):
        '''
        this method is used to find the datatypes of the columns from a dataframe.

        Args:
            df (pd.DataFrame): the input dataframe
        
        Returns:
            None
        '''
        print(df.dtypes)

    @staticmethod
    def statistics(df):
        # return transposed .describe() as large number of columns.
        '''
        this method is used to describe the statistics of the dataframe columns, particularly the numerical ones.

        Args:
            df (pd.DataFrame): the input dataframe
        
        Returns:
            pd.DataFrame
        '''

        return df.describe().T
    
    @staticmethod
    def distinct_values(df):
        '''
        this method is used to return the unique values in a dataframe.

        Args:
            df (pd.DataFrame): the input dataframe
        
        Returns:
            pd.Series
        '''

        return df.nunique()

    @staticmethod
    def df_shape(df):
        '''
        this method is used to reuturn the shape of the dataframe

        Args:
            df (pd.DataFrame): the input dataframe
        
        Returns:
            tuple
        '''
        return df.shape()

    @staticmethod
    def percent_null(df):
        '''
        this method is used to find the % of null values in a column in the df compared to the rest of the column.

        Args:
            df (pd.DataFrame): the input dataframe
        
        Returns:
            pd.Series
        '''
        null_values = df.isnull().sum() # sum of null values
        total_values = len(df)
        percentage_null = null_values / total_values * 100
        return percentage_null
    
    @staticmethod
    def count_values(df, column):
        '''
        this method is used to count the values in a specified column in a dataframe

        Args:
            df (pd.DataFrame): the input dataframe
            column (string): the column name in df
        
        Returns:
            pd.Series
        '''
        return df[column].value_counts()
    
    @staticmethod
    def get_null_greater_than_zero(df):
        '''
        this method is used to find the % of null values in a column in a df as long as there is atleast 1 null value.

        Args:
            df (pd.DataFrame): the input dataframe
        
        Returns:
            pd.Series
        '''
        null_values = DataFrameInfo.percent_null(df)
        return null_values[null_values > 0]
    
    @staticmethod
    def find_outliers(df, column):
        '''
        this method is used to find outliers in a column in a dataframe using the IQR method.

        Args:
            df (pd.DataFrame): the input dataframe
            column (string): the name of the column in df 
        
        Returns:
            pd.Series
        '''
        Q1 = df[column].quantile(0.25) # first quartile
        Q3 = df[column].quantile(0.75) # third quartile

        IQR = Q3 - Q1 # inter-quartile range.

        outliers = df[((df[column] < (Q1 - 1.5 * IQR)) | (df[column] > (Q3 + 1.5 * IQR)))][column]
        return outliers
    