import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html, callback, clientside_callback, ClientsideFunction
from dash.dependencies import Input, Output

dash.register_page(__name__, path='/', name="Introduction")

sidebar = html.Div(
    [dbc.Nav(
            [   
                dbc.NavLink("Introduction to Dash Challenge", href="#introduction", className="sidebar-link", external_link=True),
                dbc.NavLink("Imbalanced Dataset", href="#imbalanced", className="sidebar-link", external_link=True),
                dbc.NavLink("Understanding the Data", href="#dataset", className="sidebar-link", external_link=True),
                dbc.NavLink("Machine Learning Models", href="#ml-models", className="sidebar-link", external_link=True),
                dbc.NavLink("Hyperparameters", href="#hyperparameters", className="sidebar-link", external_link=True),
                dbc.NavLink("Results", href="#results", className="sidebar-link", external_link=True),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    className="sidebar-style"
)

content = html.Div([
    html.Div([
        html.H4('Introduction', id='introduction', className="section-header"),
        html.P('''The primary focus of this challenge, set up by the Plotly-Dash team, 
               was to utilize a credit card fraud database and apply Machine Learning methods to predict future fraud.'''),
        html.P('''The project was entirely open, allowing for a comparison of different Machine Learning methods to assess 
               their effectiveness in predicting fraud. These tasks were executed in a notebook available in the repository.
               For visualization, I used Dash, a framework that enables the creation of interactive dashboards,
               facilitating comprehension of the outcomes.'''),
        html.P('''The dataset, provided by Kartik Shenoy on Kaggle, is a simulated credit card transaction dataset
               containing legitimate and fraudulent transactions from January 1st, 2019, to December 31st, 2020. 
               It covers credit cards of 1000 customers conducting transactions with a pool of 800 merchants.''')
    ], className="section-container"),
    
    html.Div([
        html.H4('Imbalanced Dataset: Oversampling and Undersampling', id='imbalanced', className="section-header"),
        html.P('''Imbalanced datasets present a common challenge in classification machine learning, 
               where one target class significantly outweighs the others in terms of observations.'''), 
        html.P('''For example, a dataset with a 1:100 class imbalance could yield a 99% accuracy rate by simply 
               predicting the majority class every time, despite the model not truly learning anything about the 
               minority class.'''),
        html.Div([
            html.Div([
                html.Img(src='/assets/balanced_marcin_rutecki.png', className="section-image"),
                html.P('''This extreme class imbalance means that a naive model that always predicts 
                    genuine transactions would achieve an accuracy of 99.8%, despite being practically
                    useless for fraud detection. This is an example of a balanced dataset 
                    versus an imbalanced one (actual case).''', className='Image-text')
            ], className='Image-Conteiner'),
            html.Div([
                html.Img(src='/assets/myplot.png', className="section-image"),
                html.P('''This is the current scenario, where a significant imbalance between normal and fraudulent classes can be observed. 
                    In this dataset, non-fraudulent data is 190 times larger than fraudulent data.
                    There are several strategies that can be used. One of them is oversampling, that
                    involves increasing the size of the minority class by generating new samples, 
                    using for example SMOTE (Synthetic Minority Over-sampling Technique) which creates new
                    synthetic samples based on existing ones.
                    On the other hand, undersampling involves reducing the size of the majority class to 
                    balance the class distribution. This is achieved by randomly removing samples from the majority
                    class until the proportion between the classes is adjusted. 
                    Both strategies have their advantages and disadvantages. In this case, I chose undersampling to
                    prevent overfitting and reduce computational burden.''',
                    className='Image-text')
            ], className='Image-Conteiner'),
        ], className="image-grid"),
        html.Img(src='/assets/balanced_imbalanced.png', className="full-width-image"),
    ], className="section-container"),
    
    html.Div([
        html.H4('Understanding the Data: Type, Features, Importance and Irrelevance', id='dataset', className="section-header"),
        html.P('''When we open the dataset we find the columns: Transaction date and time, 
               Credit card number, Merchant, Category, Amount, First name, Last name, Gender, Street,
               City, State, ZIP, Latitude, Longitude, City Population, Job, Date of Birth, 
               Transaction Number, Unix Time, Merchant Latitude, Merchant Longitude, Is Fraud.'''),
        html.Img(src='/assets/columns.png', className="section-image"),
        html.P('''For this analysis, I've chosen to exclude location-related columns. I need a model that isn't 
               solely based on specific locations. Additionally, overly specific and personal information isn't
               necessary, as I aim to generalize it to a population. I removed the date but retained the transaction 
               time. Also, I adjusted the date of birth to obtain the individual's age.

               Ultimately, I decided to retain the following information: 
               Transaction hour, Merchant, Category, Amount, Gender, City, State, City Population,
               Age and "Is Fraud". Furthermore, I normalized the data for use in the model.'''),
    ], className="section-container"),
    
    html.Div([
        html.H4('Machine Learning Models, Training, Testing and Evaluation', id='ml-models', className="section-header"),
        html.P('''Firstly, I merged the files from the test dataset and the original one.
               I attempted to apply the models with the imbalanced data and adjusted the 
               weights within the same models. However, this didn't yield optimal solutions,
               so I modified the process and performed undersampling.'''),
        html.P('''Initially, I counted all the fraudulent data and randomly selected the same amount 
               of non-fraudulent data. Once I had balanced datasets, I proceeded with the models.'''),
        html.P('''I chose the most common models currently in use, and upon running them,
               I noticed a significant difference between the latest designs, particularly 
               the boost models compared to the others.'''),
        html.P('''Among the models tested, the XGBClassifier emerged as the most effective in identifying 
               fraudulent transactions. Its robust performance surpassed that of other classifiers, demonstrating 
               superior predictive power and reliability in detecting fraudulent activities within credit card 
               transactions.'''),
    ], className="section-container"),
    
    html.Div([
        html.H4('Hyperparameters: Relevancy in this Case', id='hyperparameters', className="section-header"),
        html.P('''After reviewing the results, the top three models were selected for
               further refinement. Random hyperparameter search was attempted to enhance 
               accuracy, but the outcomes weren't particularly significant, as the most accurate 
               detection models are already optimized.'''),
    ], className="section-container"),
    
    html.Div([
        html.H4('Results', id='results', className="section-header"),
        html.P('''The competition was undoubtedly challenging. The provided dataset was utilized
               to devise a highly precise method for predicting fraud. Additionally, various comparison 
               methods were conducted, and the results are available on the Models page, with the XGB Classifier 
               identified as the best method. Furthermore, clear visualization was achieved through Plotly plots 
               integrated into Dash.'''),
    ], className="section-container"),
    
    html.Footer(
        className="footer",
        children=[
            html.H2('Designed by Pablo Avalos for educational purposes.', className='author'),
            html.Div([
                html.A(
                    html.Img(src="/assets/linkedin_icon.png", className="footer-icon"), 
                    href="https://www.linkedin.com/in/avalos-p/",
                    className="footer-link"
                ),
                html.A(
                    html.Img(src="/assets/github_icon.png", className="footer-icon"), 
                    href="https://github.com/avalos-p/dash-competition",
                    className="footer-link"
                ),
            ], className="footer-links-container")
        ]
    ),
], className="introduction-text")

layout = html.Div([
    dcc.Location(id="url"), 
    sidebar,
    html.Hr(className="sidebar-hr"), 
    content
], className="div-home")

clientside_callback(
    """
    function(pathname) {
        if (pathname && pathname.includes('#')) {
            const hash = pathname.split('#')[1];
            setTimeout(() => {
                const element = document.getElementById(hash);
                if (element) {
                    element.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            }, 100);
        }
        return window.dash_clientside.no_update;
    }
    """,
    Output('url', 'pathname'),
    Input('url', 'pathname')
)