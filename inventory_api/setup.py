
from setuptools import setup, find_packages


setup(
    name='inventory_api',
    packages=find_packages('src'),
    package_dir={'': 'src'}
)