from dash import Dash, html, dash_table, dcc, callback, Output, Input
from src.utils.common_functions import charger_statistiques

# Ligues 
LIGUES = {
    'fr.1': 'Ligue 1',
    'en.1': 'Premier League',
    'de.1': 'Bundesliga',
    'es.1': 'La Liga',
    'it.1': 'Serie A'
}

# Colonnes à afficher
COLONNES = [
    {'id': 'classement', 'name': 'Pos'},
    {'id': 'nom_equipe', 'name': 'Équipe'},
    {'id': 'matchs_joues', 'name': 'J'},
    {'id': 'victoires', 'name': 'V'},
    {'id': 'nuls', 'name': 'N'},
    {'id': 'defaites', 'name': 'D'},
    {'id': 'buts_pour', 'name': 'BP'},
    {'id': 'buts_contre', 'name': 'BC'},
    {'id': 'difference_buts', 'name': 'Diff'},
    {'id': 'points', 'name': 'Pts'}
]

# Créer app
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Dashboard "),
    
    # Sélection de ligue
    dcc.RadioItems(
        id='selection-ligue',
        options=[{'label': nom, 'value': code} for code, nom in LIGUES.items()],
        value='fr.1',
        inline=True
    ),
    
    # Tableau
    html.Div(id='tableau-classement')
])

# Callback pour mettre à jour le tableau en fonction de la ligue sélectionné
@callback(
    Output('tableau-classement', 'children'),
    Input('selection-ligue', 'value')
)

# Fonction pour afficher le classement
def afficher_classement(code_ligue):
    stats = charger_statistiques(code_ligue)
    
    return dash_table.DataTable(
        data=stats.to_dict('records'), # Converti DataFrame en dictionnaire
        columns=COLONNES,
        style_header={'backgroundColor': '#1a1a2e', 'color': 'white', 'fontWeight': 'bold'},
        style_cell={'textAlign': 'center', 'padding': '10px'}
    )
# Lancer le serveur
if __name__ == '__main__':
    app.run(debug=True)