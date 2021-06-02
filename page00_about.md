---
layout: page
title: About
description: Collection of poetry related to the word "fall" in any sense of the word, with any manifestation
img: about.png # Add image post (optional)
caption: "Fall"
permalink: index.html
sidebar: true
---

---


# {{site.data.about.title}}
{{site.data.about.authors}}

{% for entry in site.data.about %}

{% if entry[0] != 'title' %}
{% if entry[0] != 'authors' %}
## {{entry[0]}}
{{entry[1]}}
{% endif %}
{% endif %}
{% endfor %}