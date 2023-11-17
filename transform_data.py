import pandas as pd


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
    def drop_columns(df):
        #drop mths_since_last_delinq, mths_since_last_record, next_payment_date and mths_since_last_major_derog (TOO MANY NULLs)
       df.drop(columns=['mths_since_last_delinq', 'mths_since_last_record', 'next_payment_date', 'mths_since_last_major_derog'], inplace=True)

       #drop Unnamed: 0 and policy_code (static value thus not important to insights)
       df.drop(columns=['Unnamed: 0', 'policy_code'], inplace=True)

    @staticmethod
    def unique_values(df):
        return df.nunique()