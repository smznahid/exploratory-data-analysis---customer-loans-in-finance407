import yaml
import pandas as pd
from sqlalchemy import create_engine


class RDSDatabaseConnector:
    '''
    A Class used to Connect to and load data from a postgres Amazon RDS database.

    Args:
        credentials (dict): argument takes a dictionary to read credentials for connecting to a RDS Database (refer to yaml_loader for more information).
    
    Attributes:
        DATABASE_TYPE (string): the type of database class will be connecting to (postgres).
        DBAPI (string): API class will be using with SQLAlchemy
        HOST (string): URL to host RDS)
        USER (string): username of SQL user.
        PASSWORD (string): password to log in to user
        DATABASE (string): the specific database the class is trying to access.
        PORT (integer): port of HOST.
    '''

    def __init__(self, credentials):
        '''
        See help(RDSDatabaseConnector) for a more accurate signature.
        '''

        self.DATABASE_TYPE = 'postgresql'
        self.DBAPI = 'psycopg2'
        self.HOST = credentials["RDS_HOST"]
        self.USER = credentials["RDS_USER"]
        self.PASSWORD = credentials["RDS_PASSWORD"]
        self.DATABASE = credentials["RDS_DATABASE"]
        self.PORT = credentials["RDS_PORT"]

    @staticmethod
    def yaml_creds_loader():
        '''
        A staticmethod used to load credential data from credential yaml file. This function will typically used to initialise the RDSDatabaseConnector class instance.

        Args:
            None
        Returns:
            credentials_dict (dict): credentials file loaded as a dictionary.
        '''

        with open('credentials.yaml', 'r') as credentials:
            credentials_dict = yaml.safe_load(credentials)
            return credentials_dict
    
    def init_engine_sqlalchemy(self):
        '''
        a method to create a SQLAlchemy engine used to extract data from a database.

        Args:
            None
        
        Returns:
            engine (class instance): engine used to load and extract data from RDS database.
        '''
        engine = create_engine(f"{self.DATABASE_TYPE}+{self.DBAPI}://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DATABASE}")
        return engine
    
    def dataframe_creator(self):
        '''
        method used to create a dataframe using engine from SQLAlchemy.

        Args:
            None
        Returns:
            pd.read_sql_table (pd.DataFrame): extracted data into a dataframe using engine.
        '''
        engine = self.init_engine_sqlalchemy()
        return pd.read_sql_table('loan_payments', engine)
    
    def save_df_to_csv(self):
        '''
        method used to save extracted dataframe into a csv file.

        Args:
            None
        Returns:
            None
        '''
        loan_payments = self.dataframe_creator()
        loan_payments.to_csv('loan_payments.csv')


if __name__ == '__main__':
    # testing script
    credentials = RDSDatabaseConnector.yaml_creds_loader()
    database = RDSDatabaseConnector(credentials)
    database.save_df_to_csv()
