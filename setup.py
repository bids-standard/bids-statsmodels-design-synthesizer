#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=3', ]

setup(
    author="John Lee",
    author_email='leej3@quansight.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="For now this is a prototype to explore the possibility of creating self-contained tool to perform the data aggregation necessary to jump from BIDS events.tsv files/model.json/other time series metadata to a design matrix for downstream implementers (or an appropriate sparse precursor of the design matrix).",
#    entry_points={
#        'console_scripts': [
#            'bids_statsmodels_design_synthesizer=bids_statsmodels_design_synthesizer.cli:main',
#        ],
#    },
    scripts=["bids_statsmodels_design_synthesizer/bids_statsmodels_design_synthesizer.py"],
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='bids_statsmodels_design_synthesizer',
    name='bids_statsmodels_design_synthesizer',
    packages=find_packages(include=['bids_statsmodels_design_synthesizer', 'bids_statsmodels_design_synthesizer.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/leej3/bids_statsmodels_design_synthesizer',
    version='0.1.0',
    zip_safe=False,
)
