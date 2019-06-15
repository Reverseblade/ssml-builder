from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ssml_builder',
    version='1.0.8',
    packages=['ssml_builder'],
    url='https://github.com/Reverseblade/ssml-builder',
    license='Free',
    author='Yuta Fujisawa',
    author_email='',
    description='SSML Builder for Alexa Skill Development in Python'
)
