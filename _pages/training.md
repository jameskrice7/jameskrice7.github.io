---
layout: single
title: "Training"
permalink: /training/
author_profile: true
---

{% for post in site.training %}
  <h2><a href="{{ post.url }}">{{ post.title }}</a></h2>
  <p>{{ post.venue }} - {{ post.date | date: "%B %d, %Y" }}</p>
  <p>{{ post.content | strip_html | truncatewords: 50 }}</p>
{% endfor %}
