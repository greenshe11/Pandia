
import pandas as pd
import matplotlib.pyplot as plt
from ipywidgets import interact
import re

from pandia.plotter import Plotter as _plotter
from pandia.widgets import Widgets as _widgets
        
class Chart:
    graph_templates = {
        # graph_templates contains code number for groups of plot, divided by its required parameters and widgets.

        0: ['bar','scatter','line','swarm', 'violin', 'box', 'boxen', 'count', 'point'],
        1: ['heatmap']
    }
    plotter = _plotter()
    widgets = _widgets()
    
    def __init__(self, data):
        # data
        self.data = pd.DataFrame(data)

        # names
        self.plot_name = None
        self.x = None
        self.y = None
        self.hue = None
        
        # objects
        self.plot_obj = None
        self.x_obj = None
        self.y_obj = None
        self.hue_obj = None
    
    def _get_plot_function(self, plot_name):
        """
        gets the plotting function in plotter class based on the graph name
        returns a function object.
        """
        return getattr(self.plotter, plot_name)
    
    def _get_plot_options(self):
        """
        gets all names of plots to be given for the plot type dropdown.
        returns all names.
        """
        plot_options = []
        for index in self.graph_templates.keys():
            for name in self.graph_templates[index]:
                plot_options.append(name)
        return plot_options
    
    def _get_template_key(self, target_name):
        """
        gets which template key a plot belongs to. see graph_templates.
        returns integer
        """
        for index in self.graph_templates.keys():
            for name in self.graph_templates[index]:
                if target_name == name:
                    return index
                
    def _get_dtypes(self):
        """
        gets all the dtypes of all columns.
        returns a list of dtypes string
        """
        temp = []
        for x in self.data.columns:
            temp.append(self.data[x].dtype)
        return temp
    
    def _get_actual_name(self, *args):
        """
        removes the dtype indicator of each name in dropdown to match feature name.
        returns tuple of strings or a string if 1 argument
        """
        converter = lambda x: re.sub(' \(.+','',x) if x is not None else x
        new = []
        single = True if len(args) == 1 else False
        for name in args:
            new.append(converter(name))
        return tuple(new) if not single else new[0]
    
    def _expand_template_0(self):
        """
        creates widgets and interactions for graph type 0
        """
        def _get_changes(**kwargs):
            try:
                self.x, self.y = kwargs['x'],kwargs['y']
                self.hue = kwargs['hue']
                self.plotter.set_data(x=self._get_actual_name(self.x), 
                                    y=self._get_actual_name(self.y), 
                                    hue=self.hue, 
                                    data=self.data)
                plot_function = self._get_plot_function(
                        plot_name = self.plot_name)
                plot_function()()
                plt.show()
                plt.close()
            except ValueError as e:
                print(f'> {e}')
        
        self.x_obj = self.widgets.add_widget(
            widget_type = self.widgets.dropdown,
            description = 'X',
            options = self.data.columns, 
            dtypes = self._get_dtypes(),
            allow_none = True)
        
        self.y_obj = self.widgets.add_widget(
            widget_type = self.widgets.dropdown,
            description = 'Y',
            options = self.data.columns, 
            dtypes = self._get_dtypes(),
            allow_none = True)
        
        self.hue_obj = self.widgets.add_widget(
            widget_type = self.widgets.dropdown,
            description = 'Hue',
            options = self.data.select_dtypes(exclude=[float]),
            allow_none = True)
        
        
        if self.x:
            self.x_obj.value = self.x
            self.y_obj.value = self.y
            self.hue_obj.value = self.hue
            
        interact(_get_changes, x=self.x_obj, y=self.y_obj, hue=self.hue_obj)
        
        
    def _expand_template_1(self):
        print('Not Yet Implemented')
    
    def _expand_entry(self, plot_name):
        """
        sets plot name and calls function based on plot name
        """
        try:
            self.plot_name = plot_name
            return getattr(self, '_expand_template_{}'.format(self._get_template_key(plot_name)))()
        except AttributeError:
            print("> specify plot")

    def build(self):
        """
        creates a gui for plotting
        """
        plot = self.widgets.add_widget(
            widget_type = self.widgets.dropdown,
            description = 'Plot',
            options = self._get_plot_options(),
            allow_none = True)
        
        interact(self._expand_entry,
                        plot_name=plot)