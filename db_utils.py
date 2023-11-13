import yaml


class RDSDatabaseConnector:

    def __init__(self, credentials):
        pass

    @staticmethod
    def yaml_loader():
        with open('credentials.yaml', 'r') as credentials:
            credentials_dict = yaml.safe_load(credentials)
            return credentials_dict
    