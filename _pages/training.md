---
layout: archive
title: "Training"
permalink: /training/
author_profile: true
---

{% assign sorted_posts = site.training | sort: 'date' | reverse %}
{% for post in sorted_posts %}
  <div class="archive__item">
    <h2 class="archive__item-title">
      <a href="{{ post.url }}">{{ post.title }}</a>
    </h2>
    <p class="archive__item-excerpt">
      {{ post.venue }} - {{ post.location }}<br>
      {{ post.date | date: "%B %d, %Y" }}
    </p>
    <p>{{ post.content | strip_html | truncate: 200 }}</p>
  </div>
{% endfor %}
