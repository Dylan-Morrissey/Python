try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
'description': 'My Project',
'author': 'Dylan Morrissey',
'url': 'https://github.com/Dylan-Morrissey/python',
'author_email': 'dylanmorrissey2010@gmail.com',
'version': 0.1,
'install_requires': [], # external packages
'packages': ['NAME'],
'scripts': [], # 'bin/script.py'
'name': 'projectname'}

setup(**config)
