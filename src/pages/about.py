from dash import html

# Style commun des cartes (même que home.py)
card_style = {
    'backgroundColor': 'white',
    'padding': '30px',
    'marginBottom': '25px'
}

layout = html.Div([
    # Bannière
    html.Div([
        html.H1("À propos", style={'margin': '0'})
    ], style={
        'background': 'linear-gradient(135deg, #1a1a2e 0%, #16213e 100%)',
        'color': 'white',
        'padding': '45px 30px',
        'marginBottom': '35px'
    }),
    
    # Objectif
    html.Div([
        html.H3("L'objectif du projet", style={'marginBottom': '15px'}),
        html.P("Ce dashboard permet de visualiser et d'analyser les données des 5 grands championnats européens de football.", 
               style={'marginBottom': '0'})
    ], style=card_style),
    
    # Technologies
    html.Div([
        html.H3("Technologies utilisées", style={'marginBottom': '15px'}),
        html.P("Python • Dash • Plotly • Pandas • OpenStreetMap", 
               style={'color': '#555', 'marginBottom': '0'})
    ], style=card_style),
    
    # Données
    html.Div([
        html.H3("Sources de données", style={'marginBottom': '15px'}),
        html.P("Les données sont récupérées au format JSON puis nettoyées et transformées en CSV. Elles ont été trouvées sur github, le lien est présent dans le FOOTER", 
               style={'marginBottom': '0'})
    ], style=card_style),
    
    # Auteurs
    html.Div([
        html.H3("Auteurs", style={'marginBottom': '15px'}),
        html.P("Dashboard développé par Rémy Kouniali et Noé Lautridou dans le cadre du projet Multidisciplinaire d'E3-FI", 
               style={'marginBottom': '0'})
    ], style=card_style)
    
], style={'padding': '25px', 'maxWidth': '900px', 'margin': '20px auto'})
