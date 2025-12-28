from dash import Dash, html, dash_table, dcc, callback, Output, Input
from src.utils.common_functions import charger_statistiques, charger_matchs, calculer_buts_par_journee,charger_locations
from src.components.header import create_header
from src.components.footer import create_footer
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

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

# Charger les locations au démarrage
LOCATIONS = charger_locations()

# Créer app
app = Dash(__name__)

app.layout = html.Div([
    create_header(),
    
    html.Div([
        html.Div([
            html.H3("Sélectionner une ligue:", style={'marginBottom': '10px'}),
            dcc.RadioItems(
                id='selection-ligue',
                options=[{'label': nom, 'value': code} for code, nom in LIGUES.items()],
                value='fr.1',
                inline=True,
                style={'marginBottom': '18px'}
            ),
        ], style={'padding': '20px', 'backgroundColor': 'white', 'borderRadius': '8px', 'marginBottom': '20px', 'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'}),
        
        html.Div([
            html.H2("Carte des stades"),
            dcc.Graph(id='carte-stades'),
        ], style={'padding': '20px', 'backgroundColor': 'white', 'borderRadius': '8px', 'marginBottom': '20px', 'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'}),
        
        html.Div([
            html.H2("Buts par journée"),
            dcc.Graph(id='graphique-buts'),
        ], style={'padding': '22px', 'backgroundColor': 'white', 'borderRadius': '8px', 'marginBottom': '20px', 'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'}),
        
        html.Div([
            html.H2("Classement"),
            html.Div(id='tableau-classement')
        ], style={'padding': '20px', 'backgroundColor': 'white', 'borderRadius': '8px', 'marginBottom': '20px', 'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'}),
    ], style={'maxWidth': '1200px', 'margin': '0 auto', 'padding': '0 20px'}),
    
    create_footer(),
])

# Callback pour mettre à jour le tableau en fonction de la ligue sélectionné
@callback(
    Output('tableau-classement', 'children'),
    Output('graphique-buts', 'figure'),
    Input('selection-ligue', 'value')
)

# Fonction pour afficher le dashboard
def afficher_dashboard(code_ligue):
    stats = charger_statistiques(code_ligue)
    matchs = charger_matchs(code_ligue)
    
    tableau = dash_table.DataTable(
        data=stats.to_dict('records'), # Converti DataFrame en dictionnaire
        columns=COLONNES,
        style_header={'backgroundColor': '#1a1a2e', 'color': 'white', 'fontWeight': 'bold'},
        style_cell={'textAlign': 'center', 'padding': '10px'}
    )

    # Graphique des buts par journée
    buts = calculer_buts_par_journee(matchs)
    fig = px.bar(x=buts.index, y=buts.values,labels={'x': 'Journée', 'y': 'Buts'})
    
    
    return tableau, fig

# Callback carte
@callback(
    Output('carte-stades', 'figure'),
    Input('selection-ligue', 'value')
)
def afficher_carte(code_ligue):
    stats = charger_statistiques(code_ligue)
    equipes_ligue = stats['nom_equipe'].tolist()
    locations_ligue = LOCATIONS[LOCATIONS['nom_equipe'].isin(equipes_ligue)].copy()
    
    # Taille des marqueurs selon capacité (8 à 30)
    min_cap = locations_ligue['capacite'].min()
    max_cap = locations_ligue['capacite'].max()
    locations_ligue['taille'] = 8 + 22 * (locations_ligue['capacite'] - min_cap) / (max_cap - min_cap)
    
    fig = go.Figure()
    fig.add_trace(go.Scattermap(
        lat=locations_ligue['latitude'],
        lon=locations_ligue['longitude'],
        mode='markers',
        marker=dict(size=locations_ligue['taille'], color='#1a1a2e', opacity=0.7),
        text=locations_ligue['nom_equipe'],
        customdata=locations_ligue[['ville', 'stade', 'capacite']],
        hovertemplate='<b>%{text}</b><br>Ville: %{customdata[0]}<br>Stade: %{customdata[1]}<br>Capacité: %{customdata[2]:,} places<extra></extra>',
    ))
    
    centres = {
        'fr.1': {'lat': 46.5, 'lon': 2.5, 'zoom': 5},
        'en.1': {'lat': 52.5, 'lon': -1.5, 'zoom': 5.5},
        'de.1': {'lat': 51, 'lon': 10, 'zoom': 5},
        'es.1': {'lat': 40, 'lon': -3.5, 'zoom': 5},
        'it.1': {'lat': 42.5, 'lon': 12, 'zoom': 5}
    }
    centre = centres.get(code_ligue, {'lat': 46.5, 'lon': 2.5, 'zoom': 5})
    
    fig.update_layout(
        map=dict(style='open-street-map', center=dict(lat=centre['lat'], lon=centre['lon']), zoom=centre['zoom']),
        margin=dict(l=0, r=0, t=0, b=0),
        height=500
    )
    return fig



# Lancer le serveur
if __name__ == '__main__':
    app.run(debug=True)