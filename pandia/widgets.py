import ipywidgets as widgets

class Widgets:
    def __init__(self):
        pass
    
    def checkbox(self, description, options, dtypes=[], allow_none=False):
        if dtypes != []:
            options = [f'{name} ({dtype})' for name,dtype in zip(options, dtypes)]
        
        if allow_none:
            options.insert(0,None)
        multibox = widgets.SelectMultiple(
        options=list(options),
        values=[list(options)[0]],
        #row: 10,
        description=description, 
        disabled=False,                           
        )

        return multibox
    
    def dropdown(self,description,options, dtypes=[],allow_none = False):
        options = list(options)
        
        if dtypes != []:
            options = [f'{name} ({dtype})' for name,dtype in zip(options, dtypes)]
        if allow_none:
            options.insert(0,None)
        dropdown = widgets.Dropdown(
            options=list(options),
            description=description,
            disabled=False)
        return dropdown
    
    def add_widget(self, widget_type, *args,**kwargs):
        return widget_type(*args,**kwargs)