from setuptools import setup

def safe_strip(string):
    if isinstance(string, str):
        return string.strip()
    else:
        try:
            return str(string)
        except Error as e:
            return ''
# Gather requirements from Conda's environment.yml so we don't have
# to worry about putting requirements in 2 places
with open('environment.yml', 'r') as ef:
    text = ef.read()
    token = "dependencies:"
    token_len = len(token)

    if token in text:
        deps_index = text.find(token)
        requirements = map(safe_strip, text[deps_index + token_len:].split('-'))
    else:
        requirements = []

setup(
    name='JobLoader',
    version='0.0.01',
    packages=['job_loader'],
    install_requires=requirements,
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.md').read(),
)
