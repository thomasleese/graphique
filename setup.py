from setuptools import find_packages, setup


with open('README.md') as file:
    long_description = file.read()

setup(
    name='graphique',
    version='0.1.0',
    description='Better charts for Python.',
    long_description=long_description,
    url='https://github.com/thomasleese/graphique',
    author='Thomas Leese',
    author_email='thomas@leese.io',
    packages=find_packages(),
    extras_require={
        'Cairo': ['cairocffi >= 0.8']
    },
    test_suite='tests'
)
