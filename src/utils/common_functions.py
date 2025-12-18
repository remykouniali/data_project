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