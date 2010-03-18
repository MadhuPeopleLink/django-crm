import os
from setuptools import setup, find_packages

packages = find_packages()
packages.remove('sample_project')
setup(
    name='django-crm',
    version='0.0.0',
    author='Caktus Consulting Group',
    author_email='solutions@caktusgroup.com',
    packages=packages,
    install_requires = [
        'Django >= 1.1,==dev', 'django-contactinfo', 'django-countries',
        'django-crumbs', 'django-notify', 'ajax_select',
        'django-pagination',
    ],
    include_package_data = True,
    exclude_package_data={
        '': ['*.sql', '*.pyc',],
        'crm': ['media/*', 'fixtures/*', 'migrations/*',],
    },
    url='http://code.google.com/p/django-crm/',
    license='LICENSE.txt',
    description='Open source Django CRM',
    long_description=open('README.txt').read(),
)
