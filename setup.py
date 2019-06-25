from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ssml_builder',
    version='1.1.1',
    packages=['ssml_builder'],
    url='https://github.com/Reverseblade/ssml-builder',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='Free',
    author='Yuta Fujisawa',
    author_email='',
    description='SSML Builder for Alexa Skill Development in Python'
)
