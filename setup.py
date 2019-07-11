try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': '',
    'author': '',
    'url': '',
    'download_url': '',
    'author_email': 'foo@mozilla.com',
    'version': "0.0.1",
    'install_requires': ['requests'],
    'packages': ['dirby'],
    'name': 'dirby'
}

setup(**config)
