from dash import html, dcc

layout = html.Div([
    html.Div([
        html.H2("Classement"),
        html.Div(id='tableau-classement')
    ], style={'padding': '20px', 'backgroundColor': 'white', 'marginBottom': '20px'}),

    html.Div([
        html.H2("Buts par journée"),
        dcc.Graph(id='graphique-buts'),
    ], style={'padding': '22px', 'backgroundColor': 'white', 'marginBottom': '20px'}),
    
    html.Div([
        html.H2("Performance Domicile vs Extérieur"),
        dcc.Graph(id='graphique-domicile-exterieur'),
    ], style={'padding': '20px', 'backgroundColor': 'white', 'marginBottom': '20px'}),
], style={'maxWidth': '1200px', 'margin': '0 auto'})
