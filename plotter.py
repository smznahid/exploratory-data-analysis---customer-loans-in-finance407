import plotly.express as px
import missingno as msno


class Plotter:
    

    @staticmethod
    def plot_boxplot(df):
        return px.box(df)


    @staticmethod
    def correlation_matrix(df):
        return px.imshow(df.corr(), title="Correlation matrix")
    
    @staticmethod
    def null_matrix(df):
        return msno.matrix(df)