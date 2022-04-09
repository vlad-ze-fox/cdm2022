## Résultats

| Equipe1 | Score1 | Score2 | Equipe2 |
| ------: | :----: | :----: | :------ |
|{% for match in site.data.resultats %}{{ match.Equipe1 }}|{{ match.Score1 }}|{{ match.Score2 }}|{{ match.Equipe2 }}|
{% endfor %}

