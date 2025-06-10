import dash
from dash import Dash, html, dcc
from dash_bootstrap_components.themes import BOOTSTRAP



app = Dash(
        __name__, 
        use_pages=True, 
        external_stylesheets=[BOOTSTRAP],
        title="Dash Competition - Fraud Detection",
        meta_tags=[
            {"name": "viewport", "content": "width=device-width, initial-scale=1"},
            {"name": "description", "content": "Credit Card Fraud Detection using Machine Learning"}
        ]
    )
app.config.suppress_callback_exceptions = True
app.layout = html.Div([
        html.H1('Dash Competition: Credit Card Fraud Detection with Machine Learning'),
        html.H2('April - 2024', className='date-project'),
        html.Div([
            dcc.Link(
                html.Button(f"{page['name']}", className='button-links'), 
                href=page["relative_path"]
            )
            for page in dash.page_registry.values()
        ], className='buttons-div'),
        dash.page_container
    ], className='app-div')


server = app.server