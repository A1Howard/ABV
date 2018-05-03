
from setuptools import setup, find_packages


setup(
    name='twilio_flask',
    packages=find_packages('src'),
    package_dir={'': 'src'}
)