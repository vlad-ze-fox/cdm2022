## Calendrier

### Phase de Poules

| Date | Groupe | Equipe1 | Equipe2 |
| ---- | ------ | ------- | ------- |
{% for match in site.data.calendrier %}{% if match.Phase != '' %}
### {{ match.Phase }}

| Date | Groupe | Equipe1 | Equipe2 |
| ---- | ------ | ------- | ------- |
{% endif %}{% if match.Groupe != '' %}|{{ match.Date }} {{ match.Heure }} | {{ match.Groupe }}| {{ match.Equipe1 }} | {{ match.Equipe2 }} |
{% else %}|{{ match.Date }} {{ match.Heure }} | {{ match.Equipe1 }} | {{ match.Equipe2 }} |
{% endif %}{% endfor %}
