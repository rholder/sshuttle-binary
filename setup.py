from setuptools import setup, find_packages

with open('requirements.txt') as file_requirements:
    requirements = file_requirements.read().splitlines()

setup(
    name='sshuttle-binary',
    version='0.78.5',
    packages=find_packages(),
    install_requires=requirements,
)
