from dash import html

layout = html.Div([
    html.H1("Bienvenue sur le Dashboard Football", style={'color': '#1a1a2e'}),
    html.P("Ce projet étudiant permet de visualiser et d'analyser les données des 5 grands championnats européens.", style={'fontSize': '18px'}),
    html.P("Utilisez le sélecteur ci-dessus pour choisir une ligue, puis naviguez via les onglets pour voir la carte ou les analyses.", style={'fontSize': '16px'}),
    html.Div([
        html.H3("Fonctionnalités:"),
        html.Ul([
            html.Li("Carte interactive des stades"),
            html.Li("Classement en temps réel"),
            html.Li("Statistiques de buts et performances")
        ], style={'textAlign': 'left', 'display': 'inline-block'})
    ], style={'marginTop': '30px'})
], style={'textAlign': 'center', 'padding': '50px', 'backgroundColor': 'white', 'borderRadius': '8px', 'margin': '20px auto', 'maxWidth': '1000px'})

