from setuptools import setup, find_packages

setup(
    name='svwebscraper',
    author=u'Florian Wörister',
    version='2022.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
    ],
    entry_points={
        'console_scripts': [
            'svscrape = svwebscraper.cli:scrape_schools',
        ],
    },
)
