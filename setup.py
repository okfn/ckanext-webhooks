from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
	name='ckanext-webhooks',
	version=version,
	description="Webhooks background job for CKAN.",
	long_description="""\
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='Open Knowledge Foundation',
	author_email='info@okfn.org',
	url='http://okfn.org',
	license='GPLv3',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.webhooks'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		# -*- Extra requirements: -*-
	],
	entry_points=\
	"""
    
    [ckan.workers]
    webhooks = ckanext.webhooks.notify:WebhooksWorker
	""",
)
