#!/usr/bin/env python

"""Tests for `bids_statsmodels_design_synthesizer` package."""

import pytest
import subprocess as sp

from bids_statsmodels_design_synthesizer import bids_statsmodels_design_synthesizer


def test_cli_help():
    output = sp.check_output(["bids_statsmodels_design_synthesizer.py","-h"])
    with pytest.raises(sp.CalledProcessError):
        output = sp.check_output(["bids_statsmodels_design_synthesizer.py","--non-existent"])
