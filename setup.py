import os
from setuptools import setup, find_packages

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name='geonode_uds',
    version='0.1',
    packages=find_packages(),
    install_requires=[
       'django-solo==1.1.2',
       'django-colorfield==0.1.10',
       'python-resize-image==1.1.10'
    ],
    include_package_data=True,
    license='BSD License',
    description='README.md',
    long_description=README,
    url='',
    author='Boundless GeoSpatial',
    author_email='',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content'
    ]
)
