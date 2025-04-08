---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Education
======
* Ph.D in Government, The University of Essex, 2027 (expected)
* MSc in Philosophy of the Social Sciences, The London School of Economics and Political Science, 2024
* MSc in Philosophy, Science and Religion, The University of Edinburgh, 2023
* Postgraduate Certificate in Philosophy and Ethics, Harvard University, 2022
* B.S. in Economics, The University of Connecticut, 2020


Work experience
======
* Spring 2025 - Present: Research Associate 
  * Oxford Computational Political Science Group
  * Oxford Internet Institute (OII) Project on Moral Contagion
  * Supervisor: Calvin Yixiang Cheng
* 2023 - 2024: Frederic Bastiat Fellow
  * Fellow at the Mercatus Center at George Mason University
  * Attended four in-person political economy colloquia in Fairfax, VA
  
Skills
======
* Programming:
  * R
  * Python
  * LaTeX
* Version Control:
  * GitHub
  * Git
* Other Skills:
  * MS Office


Publications
======
<ul>
  {% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}
</ul>

Working Papers
======
<ul>
  {% for post in site.working_papers reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}
</ul>

Talks
======
<ul>
  {% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html %}
  {% endfor %}
</ul>

<!--
Teaching
======
  <ul>{% for post in site.teaching reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
-->
  
Service and leadership
======
  <ul>{% for post in site.service_and_leadership reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
