===================================
bids-statsmodels-design-synthesizer
===================================


.. image:: https://img.shields.io/pypi/v/bids_statsmodels_design_synthesizer.svg
        :target: https://pypi.python.org/pypi/bids_statsmodels_design_synthesizer

.. image:: https://img.shields.io/travis/leej3/bids_statsmodels_design_synthesizer.svg
        :target: https://travis-ci.com/leej3/bids_statsmodels_design_synthesizer

.. image:: https://readthedocs.org/projects/bids-statsmodels-design-synthesizer/badge/?version=latest
        :target: https://bids-statsmodels-design-synthesizer.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




For now this is a prototype to explore the possibility of creating self-contained tool to perform the data aggregation necessary to jump from BIDS events.tsv files/model.json/other time series metadata to a design matrix for downstream implementers (or an appropriate sparse precursor of the design matrix).


* Free software: MIT license
* Documentation: https://bids-statsmodels-design-synthesizer.readthedocs.io.

Developer setup
--------
While this tool attempts to have no dependencies, the development dependencies for now can be installed with:

```
conda create -n bids-stats-synth python=3
conda activate bids-stats-synth
pip install -r requirements_dev.txt
```

Features
--------

* TODO

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
