from distutils.core import setup

with open('requirements.txt') as reqs:
    requirements = reqs.read().splitlines()

setup(
    name='JobLoader',
    version='0.0.01',
    packages=['job_loader'],
    install_requires=requirements,
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.md').read(),
)