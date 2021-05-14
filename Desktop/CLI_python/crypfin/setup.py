from setuptools import setup

setup(
    name = 'crypfin',
    version = '1.0.0',
    packages = ['crypfin'],
    entry_points = {
        'console_scripts': [
            'crypfin = crypfin.__main__:main'
        ]
    })
