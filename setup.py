"""Setup script of sesql-django-16"""
from setuptools import setup
from setuptools import find_packages

setup(
    name='sesql-django-16',
    version='1.0.dev',

    description='SeSQL ORM backend for Django 1.6',
    long_description=open('README.rst').read(),
    keywords='sesql, django',

    author='Fantomas42',
    author_email='fantomas42@gmail.com',
    url='https://github.com/liberation/sesql-django-16',

    packages=find_packages(),
    classifiers=[
        'Framework :: Django',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules'],

    license='BSD License'
)
