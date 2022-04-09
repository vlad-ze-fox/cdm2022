## Calendrier

| Date | Groupe | Equipe1 | Equipe2 |
| ---- | ------ | ------- | ------- |
{% for match in site.data.calendrier %}| {{ match.Date }} {{ match.Heure }} | {{ match.Groupe }}| {{ match.Equipe1 }} | {{ match.Equipe2 }} |
{% endfor %}
