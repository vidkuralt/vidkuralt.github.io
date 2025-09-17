---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

You can also find my articles on <u><a href="https://scholar.google.fr/citations?user=pqpxh7IAAAAJ">my Google Scholar profile</a>.</u>

{% include base_path %}
<ol reversed>
{% for post in site.publications reversed %}
  {% include archive-publi.html %}
{% endfor %}
</ol>
