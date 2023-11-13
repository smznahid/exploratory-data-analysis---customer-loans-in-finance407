import yaml


class RDSDatabaseConnector:
    '''
    A Class used to Connect to and load data from an Amazon RDS database.

    Args:
        credentials (dict): argument takes a dictionary to read credentials for connecting to a RDS Database (refer to yaml_loader for more information).
    
    Attributes:
        DATABASE_TYPE (string): the type of database class will be connecting to.
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
    def yaml_loader():
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
    