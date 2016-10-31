from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='xians',
    version='0.1.3',

    description='A Xian server',
    long_description=long_description,


    url='https://github.com/Kuba77/Xian-S',

    author='Jakub Chronowski',
    author_email='jakub@chronow.ski',

    license='MIT',


    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: XIAN Collaborators',
        'Topic :: Software Development :: Database',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2.7'
    ],

    keywords='xian server',
    packages=['xians', 'xians.controllers'],
    package_data={'xians': ['app.cfg']},

    install_requires=[
        'Flask==0.11.1',
        'Flask-RESTful==0.3.5',
        'flask-log==0.1.0',
        'Flask-JWT',
        'xianc',
        'xiandb'
    ],
    dependency_links=[
        'https://github.com/Kuba77/Xian-C/tarball/master#egg=xiandc',
        'https://github.com/Kuba77/Xian-DB/tarball/master#egg=xiandb',
        'https://github.com/Kuba77/flask-jwt/tarball/master#egg=Flask-JWT'
    ],
    zip_safe=False
)
