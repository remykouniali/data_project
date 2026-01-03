from dash import html, dcc

layout = html.Div([
    html.Div([
        html.H2("Classement"),
        html.Div(id='tableau-classement')
    ], style={'padding': '20px', 'backgroundColor': 'white', 'borderRadius': '8px', 'marginBottom': '20px', 'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'}),

    html.Div([
        html.H2("Buts par journée"),
        dcc.Graph(id='graphique-buts'),
    ], style={'padding': '22px', 'backgroundColor': 'white', 'borderRadius': '8px', 'marginBottom': '20px', 'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'}),
    
    html.Div([
        html.H2("Performance Domicile vs Extérieur"),
        dcc.Graph(id='graphique-domicile-exterieur'),
    ], style={'padding': '20px', 'backgroundColor': 'white', 'borderRadius': '8px', 'marginBottom': '20px', 'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'}),
], style={'maxWidth': '1200px', 'margin': '0 auto'})
