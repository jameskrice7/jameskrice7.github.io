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
* December 2025 - Present: Teaching Assistant
  * University College London (UCL) Department of Political Science
    * Introduction to Quantitative Research Methods (POLS0008)
    * Science, Scientific Discovery and Statistics (POLS0060)
* November 2025 - Present: Research Fellow
  * Earth System Governance Project
* August 2025 - Present: Ronald Coase Fellowship
  * The Mercatus Center at George Mason University
* July 2025 - August 2025: Teaching Assistant
  * Essex Summer School in Social Science Data Analysis (TA for two courses)
    * Introduction to Quantitative Text Analysis
    * Quantitative Data Analysis and Statistical Graphics with R
* March 2025 - Present: Research Associate in Online Moral Contagion at Oxford Internet Institute (OII)
  * Oxford Computational Political Science Group
* September 2023 - June 2024: Frédéric Bastiat Fellowship
  * The Mercatus Center at George Mason University
  
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
