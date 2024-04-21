import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html, callback
from dash.dependencies import Input, Output

dash.register_page(__name__, path='/',name="Introduction")

sidebar = html.Div(
    [dbc.Nav(
            [   
                dbc.NavLink("Introduction to Dash Challenge", href="#introduction",className="sidebar-link",external_link=True),
                dbc.NavLink("Imbalanced Dataset", href="#imbalanced",className="sidebar-link",external_link=True),
                dbc.NavLink("Understanding the Data", href="#dataset",className="sidebar-link",external_link=True),
                dbc.NavLink("Machine Learning Models", href="#ml-models",className="sidebar-link",external_link=True),
                dbc.NavLink("Hyperparemeters", href="#hyperparemeters",className="sidebar-link",external_link=True),
                dbc.NavLink("Results", href="#results",className="sidebar-link",external_link=True),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    className="sidebar-style"
)


content = html.Div([
            html.Div([
                html.H4('Introduction',id='introduction'),
                html.H5('''In this Dash challenge introduction, our primary goal is to delve into 
                        the analysis of a credit card fraud transaction dataset, employing both Machine 
                        Learning methodologies and Dash techniques. Through this project, we aim to scrutinize 
                        the intricate patterns within the dataset, aiming to uncover insights that could aid in 
                        fraud detection and prevention strategies.

                        Our objective revolves around a thorough examination of the credit card fraud transaction dataset.
                        To achieve this, we'll harness the power of Python alongside an array of Machine Learning models,
                        leveraging their capabilities to sift through the data and extract meaningful information. 
                        Additionally, we'll utilize Dash, a powerful framework, to visualize our findings and craft 
                        interactive dashboards, facilitating a deeper understanding of the dataset's nuances and potential 
                        fraud indicators.'''),
                html.Img(src='/assets/test.png', className='imagen-clase')
            ]),
            html.Div([
                html.H4('Imbalanced Dataset: Oversampling and Undersampling',id='imbalanced'),
                html.H5('''Imbalanced datasets present a common challenge in classification machine learning,
                         where one target class significantly outweighs the others in terms of observations.
                         This skew in class distribution, such as ratios of 1:100 or 1:1000 between minority 
                        and majority classes, can pose difficulties for traditional classification models. 
                        For instance, achieving high classification accuracy, even as high as 90% or 99%, may 
                        seem impressive, but it can be deceiving in the context of imbalanced datasets. Take,
                         for example, a dataset with a 1:100 class imbalance; simply predicting the majority 
                        class every time could yield a 99% accuracy rate, despite the model not truly learning 
                        anything about the minority class.
                        Using accuracy as a performance metric in imbalanced datasets can be misleading. In such scenarios,
                         accuracy scores are often inflated due to the dominance of the majority class. For instance, in 
                        our dataset, genuine transactions make up 99.8% of the data, while fraudulent transactions 
                        represent only 0.173%. This extreme class imbalance means that a naive model that always predicts 
                        genuine transactions would achieve an accuracy of 99.8%, despite being practically useless for fraud 
                        detection. Hence, alternative evaluation metrics, such as precision, recall, or F1-score, are 
                        typically preferred when dealing with imbalanced datasets to provide a more accurate assessment of 
                        model performance.'''),
                html.Img(src='/assets/test.png', className='imagen-clase')
            ]),
            html.Div([
                html.H4('Understanding the Data: type, features, importance and irrelevance',id='dataset'),
                html.H5('Real  test'),
                html.Img(src='/assets/test.png', className='imagen-clase')
            ]),
            html.Div([
                html.H4('Machine Learning Models: Tests, trains and evaluations',id='ml-models'),
                html.H5('Real  test'),
                html.Img(src='/assets/test.png', className='imagen-clase')
            ]),
            html.Div([
                html.H4('Hyperparemeters: relevancy in this case',id='hyperparemeters'),
                html.H5('Real  test'),
                html.Img(src='/assets/test.png', className='imagen-clase')
            ]),
            html.Div([
                html.H4('Results: Interpretation and interesting facts',id='results'),
                html.H5('Real  test'),
                html.Img(src='/assets/test.png', className='imagen-clase')
            ]),
], className="introduction-text")


layout = html.Div([dcc.Location(id="url"), sidebar,html.Hr(className="sidebar-hr"), content ],className="div-home")


