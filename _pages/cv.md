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
* December 2025 - June 2026: Teaching Assistant
  * University College London (UCL) Department of Political Science
    * Introduction to Quantitative Methods
* July 2025 - August 2025: Teaching Assistant
  * Essex Summer School in Social Science Data Analysis (TA for two courses)
    * Introduction to Quantitative Text Analysis
    * Quantitative Data Analysis and Statistical Graphics with R   
* Spring 2025 - Present: Research Associate 
  * Oxford Computational Political Science Group
  * Oxford Internet Institute (OII) and Oxford Department of Politics and International Relations (DPIR) Project on Moral Contagion
  
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
