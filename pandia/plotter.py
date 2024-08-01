
import seaborn as sns

class Plotter:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        
    def bar(self):
        return self.get_plot(sns.barplot, **self.kwargs)
    
    def scatter(self):
        return self.get_plot(sns.scatterplot, **self.kwargs)
    
    def line(self):
        return self.get_plot(sns.lineplot, **self.kwargs)
    
    def swarm(self):
        return self.get_plot(sns.swarmplot, **self.kwargs)
    
    def violin(self):
        return self.get_plot(sns.violinplot, **self.kwargs)
    
    def box(self):
        return self.get_plot(sns.boxplot, **self.kwargs)
    
    def boxen(self):
        return self.get_plot(sns.boxenplot, **self.kwargs)
    
    def count(self):
        return self.get_plot(sns.countplot, **self.kwargs)
    
    def point(self):
        return self.get_plot(sns.pointplot, **self.kwargs)
    
    
    def set_data(self, **kwargs):
        """
        sets data to be used by plotter
        """
        self.kwargs = kwargs

    def get_plot(self,plot_obj, **kwargs):
        """
        returns function based on the type of plot passed on plot_obj
        """
        return lambda: plot_obj(**kwargs)
    