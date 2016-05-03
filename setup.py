from setuptools import setup, find_packages

with open('requirements.txt') as file_requirements:
    requirements = file_requirements.read().splitlines()

setup(
    name='sshuttle',
    version='0.78.0',
    packages=find_packages(),
    install_requires=requirements,
)
