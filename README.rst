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


===================================
 Project migrated !!!!!
===================================

Efforts migrated to: https://github.com/bids-standard/pybids/pull/724


For now this is a prototype to explore the possibility of creating self-contained tool to perform the data aggregation necessary to jump from BIDS events.tsv files/model.json/other time series metadata to a design matrix for downstream implementers (or an appropriate sparse precursor of the design matrix).

Design notes: https://hackmd.io/QdwXR8XwRcmZaXp1zw6Ukg


* Free software: MIT license
* Documentation: https://bids-statsmodels-design-synthesizer.readthedocs.io.

Developer setup
--------
While this tool attempts to have no dependencies, the development dependencies for now can be installed with (very hacky for now):
::
   # you may need to brew install git-annex
   # first step is to install git-annex with something like:
   brew install git-annex
   conda create -c conda-forge -n bids-stats-synth python=3
   conda activate bids-stats-synth
   
   pip install datalad
   pip install -r requirements_dev.txt
   pip install -e .
   
   mkdir tests/data
   cd tests/data
   datalad install ///openneuro/ds000003
   mkdir ds000003/models
   curl -fsSL https://raw.githubusercontent.com/poldracklab/fitlins/master/examples/models/ds000003/models/model-001_smdl.json > ds000003/models/model-001_smdl.json
   
   cd ..
   pytest


Features
--------

Works for at least one test case!

TODO
----
- Try to get some transformations working without dependencies.
- Deal with the absence of dependicies gracefully.
- Get a single file implementation built with https://github.com/Akrog/pinliner.
- Drop boutiques.
- Write up a description of the transformation spec.
- Translation to formats easy for other implmenters to injest.
- Maybe a way to stop prior to densifying transformation.

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
