"""
Script de récupération des données de matchs.
Charge les données depuis les fichiers JSON sources.
"""

import pandas as pd
import json
import os

# Liste des ligues disponibles
LIGUES = {
    'fr.1': 'Ligue 1 (France)',
    'en.1': 'Premier League (Angleterre)',
    'de.1': 'Bundesliga (Allemagne)',
    'es.1': 'La Liga (Espagne)',
    'it.1': 'Serie A (Italie)',
}


def charger_matchs_ligue(code_ligue):
    """
    Charge les données de matchs depuis un fichier JSON de ligue.
    
    Args:
        code_ligue: Code de la ligue
    
    Returns:
        DataFrame: Données des matchs
    """
    chemin_json = f'data/raw/{code_ligue}.json'
    
    if not os.path.exists(chemin_json):
        raise FileNotFoundError(f"Le fichier {chemin_json} n'existe pas.")
    
    with open(chemin_json, 'r', encoding='utf-8') as f:
        donnees = json.load(f)
    
    liste_matchs = []
    
    for match in donnees['matches']:
        donnees_match = {
            'ligue': code_ligue,
            'journee': match['round'],
            'date': match['date'],
            'heure': match.get('time', ''),
            'equipe1': match['team1'],
            'equipe2': match['team2'],
        }
        
        # Extraction des scores
        score = match.get('score', {})
        
        # Scores mi-temps
        mt = score.get('ht', [None, None])
        donnees_match['score_equipe1_mt'] = mt[0] if len(mt) > 0 else None
        donnees_match['score_equipe2_mt'] = mt[1] if len(mt) > 1 else None
        
        # Scores temps plein
        ft = score.get('ft', [None, None])
        donnees_match['score_equipe1_final'] = ft[0] if len(ft) > 0 else None
        donnees_match['score_equipe2_final'] = ft[1] if len(ft) > 1 else None
        
        liste_matchs.append(donnees_match)
    
    df = pd.DataFrame(liste_matchs)
    df['date'] = pd.to_datetime(df['date'])
    
    return df


def charger_toutes_les_ligues():
    """
    Charge les données des ligues disponibles.
    
    Returns:
        DataFrame: Données combinées de toutes les ligues
    """
    tous_les_matchs = []
    
    for code_ligue in LIGUES.keys():
        try:
            df = charger_matchs_ligue(code_ligue)
            tous_les_matchs.append(df)
            print(f"Chargé {len(df)} matchs de {LIGUES[code_ligue]}")
        except FileNotFoundError:
            print(f"Fichier {code_ligue}.json non trouvé, ignoré")
    
    if tous_les_matchs:
        return pd.concat(tous_les_matchs, ignore_index=True)
    return pd.DataFrame()


def sauvegarder_donnees_brutes():
    """
    Charge les données depuis les fichiers JSON et sauvegarde en CSV.
    """
    os.makedirs('data/raw', exist_ok=True)
    
    # Charger et sauvegarder chaque ligue séparément
    for code_ligue in LIGUES.keys():
        try:
            df = charger_matchs_ligue(code_ligue)
            df.to_csv(f'data/raw/matchs_{code_ligue}.csv', index=False)
            print(f" Sauvegardé matchs_{code_ligue}.csv ({len(df)} matchs)")
        except FileNotFoundError:
            pass
    
    # Charger et sauvegarder toutes les ligues combinées
    df_tous = charger_toutes_les_ligues()
    if not df_tous.empty:
        df_tous.to_csv('data/raw/matchs_tous.csv', index=False)
        print(f"\n Total: {len(df_tous)} matchs sauvegardés dans matchs_tous.csv")
    
    return df_tous


if __name__ == '__main__':
    sauvegarder_donnees_brutes()