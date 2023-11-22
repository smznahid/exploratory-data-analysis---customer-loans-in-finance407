import plotly.express as px
import missingno as msno
import seaborn as sns
import matplotlib.pyplot as plt


class Plotter:
    

    @staticmethod
    def plot_boxplot(df):
        return px.box(df)


    @staticmethod
    def plot_hist(df, col):
        return df[col].hist(bins=100)

    @staticmethod
    def correlation_matrix(df):
        return px.imshow(df.corr(), title="Correlation matrix")
    
    @staticmethod
    def null_matrix(df):
        return msno.matrix(df)
    
    @staticmethod
    def plot_proportions(df, x_column, column):
        x, y, hue = x_column, "proportion", column

        df[x].groupby(df[hue], observed=False).value_counts(normalize=True).rename(y).reset_index().pipe((sns.barplot, "data"), x=x, y=y, hue=hue)