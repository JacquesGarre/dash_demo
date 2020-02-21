# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'),

    html.Div(children='''
        Dash: Dash demo pour l'application Simplon.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': ["Ulysse", 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'Nancy'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Metz'},
            ],
            'layout': {
                'title': 'Visualisation de données'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)