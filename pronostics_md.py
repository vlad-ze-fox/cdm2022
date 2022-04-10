"""
pour mettre à jour les fichiers markdown du site pronostic
© Vladimir Renard, 2022
"""

# IMPORT #######################################################################

import shutil
import csv

#  FONCTIONS ###################################################################

def csv_get(filename, encoding='utf-8', delimiter=',', quotechar='"'):
    tab = []
    with open(filename, 'r', encoding=encoding) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=delimiter, quotechar=quotechar)
        for row in csvreader:
            tab.append(row)
    return tab

def joueurs_get():
    with open('docs/_data/joueurs.csv', 'r', encoding='utf-8') as fic:
        content = fic.read()
    joueurs = sorted(content.split('\n')[1:])
    while len(joueurs)>0 and joueurs[0]=='':
        joueurs = joueurs[1:]
    return joueurs

def pronos_file_create(phase, joueur):
    """crée le fichier csv à remplir par le joueur

    Args:
        phase (integer): 0 (phase de poule) à 4 (finales)
        joueur (string): nom du joueur
    """
    shutil.copy('docs/_data/pronostics/template' + str(phase) + '.csv', 'docs/_data/pronostics/'+ str(phase) + '_' + joueur + '.csv')

def resultats_generate_md():
    res = resultats_get()
    cal = csv_get('docs/_data/calendrier.csv')
    matches = [[e[4],e[5]] for e in cal[1:] if len(e)==6]   # elem[0] = equipe1, elem[1] = equipe2
    
    completed_res = []
    for r in res:
        if r[0]=='':
            break
        completed_res.append(r.copy())
            
    with open('docs/resultats.md', 'w', encoding='utf-8') as fic:
        fic.write('## Résultats\n\n')
        fic.write('#')
        if len(completed_res)>0:
            fic.write('|'.join(['Equipe1','Score1','Score2','Equipe2'])+'\n')
            fic.write('|'.join(['----:',':---:',':---:',':----'])+'\n')
            for index, r in enumerate(completed_res):
                row = [matches[index][0], r[0], r[1], matches[index][1]]
                fic.write('|'.join(row)+'\n')

def resultats_get():
    """retourne un tableau: index = match index, value = [score1, score2]"""
    res = csv_get('docs/_data/resultats.csv')
    res = res[1:]   # enlève la première ligne (titre des champs)
    res = [[e[1],e[2]] for e in res if len(e)==4]
    return res

# MAIN #########################################################################

resultats_generate_md()
