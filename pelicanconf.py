#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Moutii RIABI'
SITENAME = 'Moutii RIABI resume'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

THEME = "./pelican-themes/resume"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PORT = 80
BIND = '0.0.0.0'

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#Profile information
NAME = 'Moutii RIABI'
TAGLINE = 'ETUDIANT'
PIC = 'profile.jpg'

#sidebar links
EMAIL = 'riabimoutii@hotmail.fr'
PHONE = '(+216) 53524911'
LINKEDIN = 'moutii-riabi'
GITHUB = 'moutii96'

CAREER_SUMMARY = 'Je suis un ingénieur en développement logiciel, je suis à la recherche d\'un stage de fin d\'étude pour prouver mes compétences'

SKILLS = [
	{
		'title': 'JAVA',
   		'level': '90'
   	},
  	{
  		'title': 'Python',
  		'level': '90'
  	},
    {
  		'title': 'C++',
  		'level': '85'
  	},
    {
  		'title': 'HTML5 &amp; CSS',
  		'level': '95'
  	},
  	{
  		'title': 'Javascript &amp; jQuery',
   		'level': '95'
   	},
  	{
  		'title': 'Dart',
  		'level': '80'
  	}
]

PROJECT_INTRO = 'Voici quelques projets que j\'ai réalisé durant mon cursus'

PROJECTS = [
	{
		'title': 'Application de  gestion de parking',
		'tagline': 'Concevoir et mettre en place une application qui aide à la gestion des données liés aux trafic des voitures utilisées par une entreprise et le calcul du plus court chemin parcouru.'
	},
	{
		'title': 'ISI Mobile',
		'tagline': 'Réalisation d\'une application mobile pour faciliter l\'accès des étudiants aux services administratifs par l\'invocation des web-service en utilisant le framework "Flutter".'
	},
	{
		'title': 'Application du tournoi football',
		'tagline': 'Contribuer à la mise en place d\'une application web pour l\'organisation d\'un tournoi de football'
	}
]

LANGUAGES = [
	{
		'name': 'Arabe',
		'description': 'Maternelle'
	},
	{
		'name': 'Français',
		'description': 'Professionnel'
	},
	{
		'name': 'Anglais',
		'description': 'Professionnel'
	},
	{
		'name': 'Allemand',
		'description': 'Amateur'
	}
]


EXPERIENCES = [
	{
		'job_title': 'Stagiaire',
		'time': 'Juillet 2020 - Août 2020',
		'company': 'Ministère de l\'Industrie et des Petites et Moyennes Entreprises',
		'details': 'Concevoir et Développer une Plateforme inter-administrations qui a pour objectif le partage et l’échange des documents administratifs entre les fonctionnaires de la ministère en utilisant le micro-framework "Flask".'	
	},
	{
		'job_title': 'Stagiaire',
		'time': 'Février 2018 - Mai 2018',
		'company': 'Société Tunisienne de l\'Electricité et du Gaz (STEG)',
		'details': ' Réalisation d\'une application de rapprochement des encaissements des partenaires externes de la "STEG" en utilisant la technologie "JEE" et en suivant la méthodologie "SCRUM".'
	},
]

EDUCATIONS = [
	{
		'degree': 'Cycle Ingénieur en Développement Logiciel',
		'meta': 'Institut Supérieur d\'Informatique (ISI)',
		'time': 'Septembre 2018 - Aujourd\'hui'
	},
	{
		'degree': 'Licence appliquée en Système Informatique et Logiciel',
		'meta': 'Institut Supérieur d\'Informatique (ISI)',
		'time': 'Septembre 2015 - Juin 2018'
	},
	{
		'degree': 'Baccalauréat (Science Expérimentale)',
		'meta': 'Lycée 02 Mars 1934, La Goulette',
		'time': '2015'
	}
]