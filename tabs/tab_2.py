import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

tab_2_layout = html.Div([
    html.H1('State Selector'),
    html.Div([
        html.Div([
            html.H6('Pick one:'),
            dcc.RadioItems(
                id='page-2-radios',
                options=[{'label': i, 'value': i} for i in ['Massachusetts', 'New Hampshire', 'Maine']],
                value='Massachusetts',
                style = dict(
                    width = '70%',
                    display = 'inline-block',
                    verticalAlign = "middle"
                    ),
            ),
        ], className='four columns'),
        html.Div([
            html.H6(id='page-2-content')
        ], className='eight columns'),
    ], className='twelve columns'),
], className='twelve columns')
