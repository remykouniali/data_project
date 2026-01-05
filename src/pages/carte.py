from dash import html, dcc

layout = html.Div([
    html.H2("Localisation des Stades"),
    html.P("Cette carte interactive affiche la position géographique de tous les stades de la ligue sélectionnée. La taille des points dépend de la capacité du stade."),
    dcc.Graph(id='carte-stades'),
], style={'padding': '20px', 'backgroundColor': 'white', 'margin': '20px auto', 'maxWidth': '1200px'})
