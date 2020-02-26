# # -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import os
import plotly.express as px


# Read csv
dir_path = os.path.dirname(os.path.realpath(__file__))
csv = os.path.join(dir_path, "liste_apprenants-devdataia.csv")
data = pd.read_csv(csv, encoding="windows-1252", sep=";") 
#print(data)
#print(data['Prénom'])
data1 = data.groupby(data['Couleur T-Shirt'])['Couleur T-Shirt'].count()
fig = px.pie(data, values= data1, names= ['noir', 'bleu', 'blanc'], title= 'Couleur de T-Shirt de la promo')



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Promotion Simplon'),
    html.H3(children='École Microsoft Dev Data-IA'),

    html.Div(children='''
        Un exemple d'utilisation du framework Dash
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': data['Prénom'], 'y': data['Année de Naissance'].fillna(0), 'type': 'bar', 'name': 'Nancy'},

            ],
            'layout': {
                'title': 'Années de naissance de la promo',
                'yaxis': {
                    'range': [1950,2005]
                }
            }
        }
    ),

    dcc.Graph(
        id='example-graph-2',
        figure= fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)