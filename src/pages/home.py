from dash import html

# Styles communs
card_style = {
    'backgroundColor': 'white',
    'padding': '30px',
    'borderRadius': '6px',
    'marginBottom': '25px',
    'boxShadow': '0 1px 3px rgba(0,0,0,0.08)'
}

layout = html.Div([
    # Bannière
    html.Div([
        html.H1("Dashboard Football Européen", style={'margin': '0 0 12px 0'}),
        html.P("Visualisation des données des 5 grandes ligues")
    ], style={
        'background': 'linear-gradient(135deg, #1a1a2e 0%, #16213e 100%)',
        'color': 'white',
        'padding': '45px 30px',
        'borderRadius': '8px',
        'marginBottom': '35px',
        'boxShadow': '0 2px 8px rgba(0,0,0,0.1)'
    }),
    
    # Introduction
    html.Div([
        html.P("Ce projet permet d'explorer les statistiques des championnats européens."),
        html.P("Sélectionnez une ligue ci-dessus, puis utilisez les onglets pour naviguer.", 
               style={'color': '#666', 'marginBottom': '0'})
    ], style=card_style),
    
    # Fonctionnalités
    html.Div([
        html.H3("Que contient ce dashboard ?", style={'marginBottom': '20px'}),
        html.Div([
            html.Strong("Carte des stades"),
            html.P("Localisation géographique des stades avec leurs capacités", 
                   style={'margin': '8px 0 20px 0', 'color': '#555'})
        ]),
        html.Div([
            html.Strong("Classements"),
            html.P("Tableaux de classement avec les stats principales", 
                   style={'margin': '8px 0 20px 0', 'color': '#555'})
        ]),
        html.Div([
            html.Strong("Statistiques"),
            html.P("Graphiques sur les buts par journée et performances domicile/extérieur", 
                   style={'margin': '8px 0 0 0', 'color': '#555'})
        ])
    ], style=card_style),
    
    # Ligues
    html.Div([
        html.H3("Ligues disponibles", style={'marginBottom': '15px'}),
        html.P("Ligue 1 • Premier League • Bundesliga • La Liga • Serie A", 
               style={'color': '#555', 'marginBottom': '0'})
    ], style=card_style)
    
], style={'padding': '25px', 'maxWidth': '900px', 'margin': '20px auto'})


