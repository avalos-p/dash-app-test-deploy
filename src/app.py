import dash
from dash import Dash, html, dcc
from dash_bootstrap_components.themes import BOOTSTRAP



app = Dash(__name__, use_pages=True, external_stylesheets=[BOOTSTRAP])
app.config.suppress_callback_exceptions = True
app.layout = html.Div([
    html.H1('Dash Competition: Credit Card transactions fraud detection with Machine Learning'),
    html.Div([
            dcc.Link(
                html.Button(f"{page['name']}", className='button-links'), 
                href=page["relative_path"]
                    )
            for page in dash.page_registry.values()
        ],className='buttons-div'),
        dash.page_container])


server = app.server