from src.utils.common_functions import charger_statistiques, charger_matchs

stats = charger_statistiques('fr.1')
match_ligue_1 = charger_matchs('fr.1')
#print(stats)
print(match_ligue_1)