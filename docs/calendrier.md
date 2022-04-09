---
food: Pizza
---

## Calendrier

<ul>
{% for match in site.data.calendrier %}
<li>
    {{ match.Equipe1 }} - {{ match.Equipe2 }}
</li>

{% endfor %}
</ul>

{{ page.food }}