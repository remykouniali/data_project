from dash import html

layout = html.Div([
    html.H1("À propos du projet", style={'color': '#1a1a2e', 'marginBottom': '20px'}),
    
    html.Div([
        html.H3("L'objectif"),
        html.P("Ce projet a pour but de visualiser et d'analyser les données des 5 grands championnats européens de football pour la saison en cours."),
        
        html.H3("Technologies utilisées", style={'marginTop': '20px'}),
        html.Ul([
            html.Li("Python (Traitement des données)"),
            html.Li("Dash & Plotly (Visualisation interactive)"),
            html.Li("Pandas (Manipulation de données)"),
            html.Li("OpenStreetMap (Cartographie)")
        ]),
        
        html.H3("Données", style={'marginTop': '20px'}),
        html.P("Les données sont récupérées au format JSON puis nettoyées et transformées en CSV pour alimenter le dashboard."),
        
        html.H3("Auteur", style={'marginTop': '20px'}),
        html.P("Développé par Rémy Kouniali et Noé Lautridou dans le cadre d'un projet étudiant.")
        
    ], style={'backgroundColor': 'white', 'padding': '30px', 'borderRadius': '10px', 'boxShadow': '0 2px 5px rgba(0,0,0,0.1)', 'textAlign': 'left'})
    
], style={'maxWidth': '800px', 'margin': '0 auto', 'padding': '40px 20px', 'textAlign': 'center'})
