## Calendrier

{% for match in site.data.calendrier %}
- {{ match.Equipe1 }} - {{ match.Equipe2 }}
{% endfor %}