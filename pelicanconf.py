#!/usr/bin/env python
# -*- coding: utf-8 -*- #
AUTHOR = 'Free Agent'
SITENAME = 'Finalmente ci sposiamo'
SITETITLE = 'Save the date: 28 Maggio 2016'
SITESUBTITLE = "Sara ha detto si!"
SITEURL = 'http://www.marcoandsara.info'


THEME = 'free-agent'
THEME_STATIC_DIR = 'theme'
STATIC_PATHS = ['images']
PATH = 'content'
#add images back in above
# EXTRA_PATH_METADATA = {
#     'static/images/portfolio': {'path': 'images/portfolio'},
#     }
TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'it'
BOOTSTRAP_FILE = 'bootstrap.min.css'
CSS_FILE = 'freeagent.css'
FONTS = 'fonts'

SCRIPTS = [
	'jquery-1.11.0.js',
	'bootstrap.min.js',
	'http://cdnjs.cloudflare.com/ajax/libs/jquery-easing/1.3/jquery.easing.min.js',
	'classie.js',
	'cbpAnimatedHeader.js',
	'jqBootstrapValidation.js',
	'contact_me.js',
	'freeagent.js'
]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DIRECT_TEMPLATES = ['index']
DELETE_OUTPUT_DIRECTORY = True
# Top Menu Links
NAVLINKS = (
	#('#page-top', 'Home'),
	('#services','Essenziale'),
	('#portfolio', 'Preparativi'),
	('#about', 'Gossip'),
	('#contact', 'Contattaci')
)

# Portfolio Name
PORTFOLIO = 'Prepariamoci insieme'



#Contact form fields sorted by: label, input_type, id, required_validation_,msg
CONTACT_FIELDS = (
	['Name', 'text', 'name', 'Please enter your name.'],
	['Email Address', 'email', 'email','Please enter your email address.' ],

	['Message', 'textarea', 'message', 'Please enter a message.']
)
