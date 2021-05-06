#!/usr/bin/env python

"""Tests for `bids_statsmodels_design_synthesizer` package."""

import pytest
import subprocess as sp

from bids_statsmodels_design_synthesizer import bids_statsmodels_design_synthesizer


def test_cli_help():
    output = sp.check_output(["bids_statsmodels_design_synthesizer.py","-h"])
    with pytest.raises(sp.CalledProcessError):
        output = sp.check_output(["bids_statsmodels_design_synthesizer.py","--non-existent"])


def test_minimal_cli_functionality():
    """
    We roughly want to implement the equivalent of the following:
    from bids.analysis import Analysis
    from bids.layout import BIDSLayout

    layout = BIDSLayout("data/ds000003")
    analysis = Analysis(model="data/ds000003/models/model-001_smdl.json",layout=layout)
    analysis.setup()

    """
    model = "model-001_smdl.json"
    bids_dir = "data/ds000003"
    events_file = "events.tsv"
    output = sp.check_output(
        f"""
        bids_statsmodels_design_synthesizer.py
        --bids-dir {bids_dir}
        --model {model}
        --events-file {events_file}
        """.split()
    )
