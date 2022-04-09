"""
pour mettre à jour les fichiers markdown du site pronostic
© Vladimir Renard, 2022
"""

# IMPORT #######################################################################

import shutil
import csv

#  FONCTIONS ###################################################################

def get_joueurs():
    with open('docs/_data/joueurs.csv', 'r', encoding='utf-8') as fic:
        content = fic.read()
    joueurs = sorted(content.split('\n')[1:])
    while len(joueurs)>0 and joueurs[0]=='':
        joueurs = joueurs[1:]
    return joueurs

def get_resultats():
    """retourne un tableau: index = match index, value = [score1, score2]"""
    res = get_csv('docs/_data/resultats.csv')
    res = res[1:]   # enlève la première ligne (titre des champs)
    res = [[e[1],e[2]] for e in res if len(e)==4]
    return res

def get_csv(filename, encoding='utf-8', delimiter=',', quotechar='"'):
    tab = []
    with open(filename, 'r', encoding=encoding) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=delimiter, quotechar=quotechar)
        for row in csvreader:
            tab.append(row)
    return tab

def create_pronos_file(phase, joueur):
    """crée le fichier csv à remplir par le joueur

    Args:
        phase (integer): 0 (phase de poule) à 4 (finales)
        joueur (string): nom du joueur
    """
    shutil.copy('docs/_data/pronostics/template' + str(phase) + '.csv', 'docs/_data/pronostics/'+ str(phase) + '_' + joueur + '.csv')

def generate_resultats_md():
    res = get_resultats()
    print(res, len(res))
    
    

# MAIN #########################################################################

generate_resultats_md()