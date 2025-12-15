"""
Script de nettoyage des données de matchs multi-ligues.
Transforme les données brutes en statistiques exploitables.
"""

import pandas as pd
import os


def calculer_statistiques_equipes(df_matchs, code_ligue=None):
    """
    Calcule les statistiques complètes pour chaque équipe.
    
    Args:
        df_matchs: DataFrame des matchs avec scores
        code_ligue: Code de la ligue (optionnel, pour filtrer)
    
    Returns:
        DataFrame: Statistiques par équipe
    """
    # Filtrer par ligue si spécifié
    if code_ligue and 'ligue' in df_matchs.columns:
        df_matchs = df_matchs[df_matchs['ligue'] == code_ligue].copy()
    
    equipes = set(df_matchs['equipe1'].unique()) | set(df_matchs['equipe2'].unique())
    statistiques = []
    
    for equipe in equipes:
        matchs_domicile = df_matchs[df_matchs['equipe1'] == equipe].copy()
        matchs_exterieur = df_matchs[df_matchs['equipe2'] == equipe].copy()
        
        victoires, nuls, defaites = 0, 0, 0
        buts_pour, buts_contre = 0, 0
        
        # Matchs à domicile
        for _, match in matchs_domicile.iterrows():
            if pd.notna(match['score_equipe1_final']) and pd.notna(match['score_equipe2_final']):
                bp = int(match['score_equipe1_final'])
                bc = int(match['score_equipe2_final'])
                buts_pour += bp
                buts_contre += bc
                if bp > bc: victoires += 1
                elif bp == bc: nuls += 1
                else: defaites += 1
        
        # Matchs à l'extérieur
        for _, match in matchs_exterieur.iterrows():
            if pd.notna(match['score_equipe1_final']) and pd.notna(match['score_equipe2_final']):
                bp = int(match['score_equipe2_final'])
                bc = int(match['score_equipe1_final'])
                buts_pour += bp
                buts_contre += bc
                if bp > bc: victoires += 1
                elif bp == bc: nuls += 1
                else: defaites += 1
        
        matchs_joues = victoires + nuls + defaites
        points = victoires * 3 + nuls
        difference_buts = buts_pour - buts_contre
        
        statistiques.append({
            'nom_equipe': equipe,
            'matchs_joues': matchs_joues,
            'victoires': victoires,
            'nuls': nuls,
            'defaites': defaites,
            'buts_pour': buts_pour,
            'buts_contre': buts_contre,
            'difference_buts': difference_buts,
            'points': points,
        })
    
    df = pd.DataFrame(statistiques)
    df = df.sort_values(
        by=['points', 'difference_buts', 'buts_pour'],
        ascending=[False, False, False]
    ).reset_index(drop=True)
    df.insert(0, 'classement', range(1, len(df) + 1))
    
    return df


def nettoyer_donnees_matchs(df_matchs):
    """
    Nettoie et enrichit les données de matchs.
    """
    df = df_matchs.copy()
    df = df[pd.notna(df['score_equipe1_final']) & pd.notna(df['score_equipe2_final'])].copy()
    df['total_buts'] = df['score_equipe1_final'].astype(int) + df['score_equipe2_final'].astype(int)
    return df


def traiter_et_sauvegarder_donnees():
    """
    Charge les données brutes, les nettoie et sauvegarde en CSV.
    """
    os.makedirs('data/cleaned', exist_ok=True)
    
    ligues = ['fr.1', 'en.1', 'de.1', 'es.1', 'it.1']
    
    # Traiter chaque ligue
    for code in ligues:
        chemin = f'data/raw/matchs_{code}.csv'
        if os.path.exists(chemin):
            df = pd.read_csv(chemin)
            df['date'] = pd.to_datetime(df['date'])
            
            stats = calculer_statistiques_equipes(df)
            stats.to_csv(f'data/cleaned/statistiques_{code}.csv', index=False)
            
            matchs = nettoyer_donnees_matchs(df)
            matchs.to_csv(f'data/cleaned/matchs_{code}_nettoyes.csv', index=False)
            
            print(f"{code}: {len(stats)} équipes, {len(matchs)} matchs")
    
    # Traiter toutes les ligues combinées
    if os.path.exists('data/raw/matchs_tous.csv'):
        df_tous = pd.read_csv('data/raw/matchs_tous.csv')
        df_tous['date'] = pd.to_datetime(df_tous['date'])
        
        matchs_tous = nettoyer_donnees_matchs(df_tous)
        matchs_tous.to_csv('data/cleaned/matchs_tous_nettoyes.csv', index=False)
        print(f"\nTotal: {len(matchs_tous)} matchs nettoyés")


if __name__ == '__main__':
    traiter_et_sauvegarder_donnees()