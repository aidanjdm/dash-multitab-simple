import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

tab_3_layout = html.Div([
    html.H1('Number Selector'),
    html.Div([
        html.Div([
            html.H6('Pick one:'),
            dcc.Slider(
                id='page-3-slider',
                min=0,
                max=100,
                step=1,
                marks={i:str(i) for i in [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]},
                value=50,
            ),
        ], className='four columns'),
        html.Div([
            html.H6(id='page-3-content')
        ], className='eight columns'),
    ], className='twelve columns'),
], className='twelve columns')
