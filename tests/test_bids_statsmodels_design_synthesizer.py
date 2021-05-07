#!/usr/bin/env python

"""Tests for `bids_statsmodels_design_synthesizer` package."""

import pytest
import subprocess as sp
from pathlib import Path

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

    more specifically we want to reimplement this line
    https://github.com/bids-standard/pybids/blob/b6cd0f6787230ce976a374fbd5fce650865752a3/bids/analysis/analysis.py#L282
    """
    boutiques_dir = Path(__file__).parent.parent / "boutiques"
    cmd = (
        f"""
        bosh
        {boutiques_dir}/bids-app-bids-statsmodels-design-synthesizer.json
        -i {boutiques_dir}/invocation.json
        -e
        -d
        """
    )
    output = sp.check_output(cmd.split())
