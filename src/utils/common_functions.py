"""
Fonction utilisees pour le dashboard"""

import pandas as pd


def charger_statistiques(code_ligue):
    """
    Charge les statistiques des équipes d'une ligue
    
    """
    return pd.read_csv(f'data/cleaned/statistiques_{code_ligue}.csv')


def charger_matchs(code_ligue):
    """
    Charge les matchs d'une ligue
    """
    df = pd.read_csv(f'data/cleaned/matchs_{code_ligue}_nettoyes.csv')
    df['date'] = pd.to_datetime(df['date'])
    return df

def calculer_buts_par_journee(matchs):
    # Extraire le numéro (Matchday 1 → 1)
    matchs['num_journee'] = matchs['journee'].str.extract(r'(\d+)').astype(int)
    
    # Grouper par numéro et sommer
    buts = matchs.groupby('num_journee')['total_buts'].sum()
    
    return buts

def charger_locations():
    """
    Charge les coordonnées des stades
    """
    return pd.read_csv('data/cleaned/locations_stades_nettoyes.csv')

def calculer_stats_domicile_exterieur(matchs, stats):
    # Buts à domicile et extérieur
    dom = matchs.groupby('equipe1')['score_equipe1_final'].sum()
    ext = matchs.groupby('equipe2')['score_equipe2_final'].sum()
    
    return pd.DataFrame({
        'equipe': stats['nom_equipe'],
        'buts_domicile': stats['nom_equipe'].map(dom).fillna(0),
        'buts_exterieur': stats['nom_equipe'].map(ext).fillna(0)
    })