import plotly.express as px

class Plotter:
    

    @staticmethod
    def plot_boxplot(df):
        return px.box(df)


    @staticmethod
    def correlation_matrix(df):
        px.imshow(df.corr(), title="Correlation matrix")