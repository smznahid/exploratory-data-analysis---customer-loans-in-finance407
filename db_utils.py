import yaml


class RDSDatabaseConnector:

    def __init__(self, credentials):
        self.DATABASE_TYPE = 'postgresql'
        self.DBAPI = 'psycopg2'
        self.HOST = credentials["RDS_HOST"]
        self.USER = credentials["RDS_USER"]
        self.PASSWORD = credentials["RDS_PASSWORD"]
        self.DATABASE = credentials["RDS_DATABASE"]
        self.PORT = credentials["RDS_PORT"]

    @staticmethod
    def yaml_loader():
        with open('credentials.yaml', 'r') as credentials:
            credentials_dict = yaml.safe_load(credentials)
            return credentials_dict
    