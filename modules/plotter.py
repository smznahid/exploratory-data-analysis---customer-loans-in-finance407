import plotly.express as px
import missingno as msno
import seaborn as sns
import matplotlib.pyplot as plt


class Plotter:
    '''
    A class used to help visualise data and plot graphs.
    '''

    @staticmethod
    def plot_boxplot(df):
        '''
        this method plots a boxplot using a dataframe

        Args:
            df (pd.DataFrame): the input dataframe
        
        Returns:
            plotly.graph_objects.Figure
        '''
        return px.box(df)


    @staticmethod
    def plot_hist(df, col):
        '''
        this method plots a histogram using a dataframe

        Args:
            df (pd.DataFrame): the input dataframe
        
        Returns:
            matplotlib.AxesSubplot: the histogram.
        '''
        return df[col].hist(bins=100)

    @staticmethod
    def correlation_matrix(df):
        '''
        this method plots a correlation matrix of a dataframe

        Args:
            df (pd.DataFrame): the input dataframe
        
        Returns:
            fig (graph_objects.Figure): the correlation matrix image.
        '''
        return px.imshow(df.corr(), title="Correlation matrix")
    
    @staticmethod
    def null_matrix(df):

        '''
        this method plots a null_matrix

        Args:
            df (pd.DataFrame): the input dataframe
        
        Returns:
            fig: the null value matrix
        '''
        return msno.matrix(df)
    
    @staticmethod
    def plot_proportions(df, x_column, column):

        '''
        this method plots the proportion of one column with another in a dataframe.

        Args:
            df (pd.DataFrame): the input dataframe
            x_column (string): x-axis column
            column (string): column to be plotting with

        Returns:
            None
        '''
        x, y, hue = x_column, "proportion", column

        df[x].groupby(df[hue], observed=False).value_counts(normalize=True).rename(y).reset_index().pipe((sns.barplot, "data"), x=x, y=y, hue=hue)